import requests

BASE_URL = "https://api.telegram.org/bot"

TOKEN = "5750208451:AAEKOMdAug0pbDaL4D2t9Mb6TRm5ueKRmiM"


def get_updates():
    r = requests.get(f'{BASE_URL}{TOKEN}/getUpdates')
    message = r.json()['result'][-1]['message']['text']
    user_id = r.json()['result'][-1]['message']['chat']['id']
    requests.get(f'{BASE_URL}{TOKEN}/sendMessage?chat_id={user_id}&text={message}')


get_updates()