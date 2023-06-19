from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


# webdriver.Chrome(ChromeDriverManager(path = r".\\Drivers").install())
chrome_path = '/Drivers/.wdm/drivers/chromedriver'
service = Service(chrome_path)
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(service=service, options=options)
driver.get('https://www.twitch.tv/pepepizza31/schedule')

time.sleep(80)
contenu_precedent = driver.page_source

while True:
    # Attendre une période de temps spécifiée
    time.sleep(10)  # Par exemple, attendre 5 secondes avant chaque vérification

    # Comparer le contenu actuel avec le contenu précédent
    contenu_actuel = driver.page_source
    print("page non updated")
    if contenu_actuel != contenu_precedent:
        # La page a été modifiée, faites quelque chose ici
        print("La page a été mise à jour !")

    # Mettre à jour le contenu précédent avec le contenu actuel pour la prochaine itération
    contenu_precedent = contenu_actuel
