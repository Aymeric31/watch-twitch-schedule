import requests
import datetime
from dotenv import load_dotenv
import os
from datetime import datetime
import json

load_dotenv()
twitch_client_id = os.environ.get('TWITCH_CLIENT_ID')
twitch_broadcaster_id = os.environ.get('TWITCH_BROADCASTER_ID')
twitch_access_token = os.environ.get('TWITCH_ACCESS_TOKEN')

headers = {
    "Client-ID": twitch_client_id,
    "Authorization": f'Bearer {twitch_access_token}'
}

url = f'https://api.twitch.tv/helix/schedule?broadcaster_id={twitch_broadcaster_id}'

response = requests.get(url, headers=headers)
data = response.json()

# Vérification si la clé "data" existe dans le dictionnaire
if 'data' in data:
    segments = data['data']['segments']
    
    # Liste pour stocker les informations extraites
    events = []
    
    # Obtenir la date actuelle
    date_actuelle = datetime.now()
    
    # Obtenir le numéro de la semaine actuelle
    semaine_actuelle = date_actuelle.isocalendar()[1]

    # Parcourir chaque segment
    for segment in segments:
        segment_id = segment['id']
        start_time = segment['start_time']
        end_time = segment['end_time']
        title = segment['title']
        is_recurring = segment['is_recurring']
        # Vérifier si le champ 'category' est présent et obtenir l'ID de la catégorie
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
            
        # Obtenir la date de début de l'événement
        event_start_date = datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%S%z")

        # Obtenir le numéro de la semaine de l'événement
        event_week = event_start_date.isocalendar()[1]

        # Vérifier si l'événement se déroule dans la semaine actuelle
        if event_week == semaine_actuelle:
            # Créer un dictionnaire pour stocker les informations de l'événement actuel
            event = {
                'segment_id': segment_id,
                'start_time': start_time,
                'end_time': end_time,
                'title': title,
                'category_id': category_id,
                'category_name': category_name,
                'is_recurring': is_recurring
            }
        
            # Ajouter le dictionnaire de l'événement à la liste des événements
            events.append(event)
        else:
            print("Event non présent dans la semaine en cours")
    # Trier les segments par date dans l'ordre croissant
    events.sort(key=lambda x: x['start_time'])
    
    # Écrire les données dans un fichier JSON
    with open('events-new.json', 'w') as json_file:
        json.dump(events, json_file, indent=4)
    
    print("Les données ont été enregistrées dans events.json.")
else:
    print("Clé 'data' introuvable dans le dictionnaire.")
