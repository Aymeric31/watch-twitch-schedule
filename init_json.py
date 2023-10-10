import requests
import datetime
from dotenv import load_dotenv
import os
from datetime import datetime
import json

# Load environment variables
load_dotenv()
twitch_client_id = os.environ.get('TWITCH_CLIENT_ID')
twitch_broadcaster_id = os.environ.get('TWITCH_BROADCASTER_ID')
twitch_access_token = os.environ.get('TWITCH_ACCESS_TOKEN')

# Set Twitch API headers
headers = {
    "Client-ID": twitch_client_id,
    "Authorization": f'Bearer {twitch_access_token}'
}

# Define the Twitch API URL
url = f'https://api.twitch.tv/helix/schedule?broadcaster_id={twitch_broadcaster_id}'

# Send a GET request to the Twitch API
response = requests.get(url, headers=headers)
data = response.json()

# Check if the 'data' key exists in the API response
if 'data' in data:
    segments = data['data']['segments']
    
    # List to store extracted event information
    events = []
    
    # Get the current date and week number
    current_date = datetime.now()
    current_week = current_date.isocalendar()[1]

    # Iterate through each segment
    for segment in segments:
        # Extract segment data
        segment_id = segment['id']
        start_time = segment['start_time']
        end_time = segment['end_time']
        title = segment['title']
        is_recurring = segment['is_recurring']
        
        # Check if the 'category' field is present and obtain the category ID.
        if segment['category'] is not None:
            if segment['category']['id'] and segment['category']['name'] is not None:
                category_id = segment['category']['id']
                category_name = segment['category']['name']
            else:
                category_id = None
                category_name = None
        else:
            category_id = None
            category_name = None
            
        # Convert start_time to a datetime object
        event_start_date = datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%S%z")
        
        # Get week and day of the event
        event_week = event_start_date.isocalendar()[1]
        event_day = event_start_date.isocalendar()[2]

        # Extract hour from start_time and end_time
        start_time = datetime.strptime(segment['start_time'], "%Y-%m-%dT%H:%M:%S%z")
        start_time_hour = start_time.strftime("%H:%M")
        
        end_time = datetime.strptime(segment['end_time'], "%Y-%m-%dT%H:%M:%S%z")
        end_time_hour = end_time.strftime("%H:%M")

        # Check if the event is in the current week
        if event_week == current_week:
            # Create an event dictionary
            event = {
                'start_time': start_time_hour,
                'end_time': end_time_hour,
                'event_day': event_day,
                'title': title,
                'category_id': category_id,
                'category_name': category_name,
                'is_recurring': is_recurring
            }
        
            # Add the event dictionary to the list of events
            events.append(event)
        else:
            print(f"Event from {event_start_date} not present in the current week")
    
    # Sort events by start_time
    events.sort(key=lambda x: x['event_day'])
    
    # Write the data to a JSON file
    with open('events.json', 'w') as json_file:
        json.dump(events, json_file, indent=4)
    
    print("Data has been saved in events-new.json.")
else:
    print("Key 'data' not found in the dictionary.")
