import requests
import time
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
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

contenu_precedent = None

while True:
    response = requests.get(url, headers=headers)
    data = response.json()

    # Vérifier si la requête a réussi
    if response.status_code == 200:
        contenu_actuel = data  # Stocker les données actuelles

        # Vérifier si les détails du planning ont changé
        if contenu_precedent is not None and contenu_actuel != contenu_precedent:
            date_actuelle = datetime.now()
            debut_semaine = date_actuelle - timedelta(days=date_actuelle.weekday())
            fin_semaine = debut_semaine + timedelta(days=6)

            evenements_precedents = {event["id"] for event in contenu_precedent["data"] if debut_semaine <= datetime.fromisoformat(event["start_time"].rstrip('Z')) <= fin_semaine}
            evenements_actuels = {event["id"] for event in contenu_actuel["data"] if debut_semaine <= datetime.fromisoformat(event["start_time"].rstrip('Z')) <= fin_semaine}

            evenements_supprimes = evenements_precedents - evenements_actuels
            evenements_ajoutes = evenements_actuels - evenements_precedents

            if evenements_supprimes or evenements_ajoutes:
                print("La page a été mise à jour !")

                # Effectuer les actions souhaitées sur la mise à jour détectée
                # Par exemple, publier un tweet ou un message sur Discord

        contenu_precedent = contenu_actuel

    # Attendre une période de temps spécifiée
    time.sleep(10)  # Pause d'une minute
