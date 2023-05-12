import requests
BASE_URL = 'https://api.telegram.org/bot'

TOKEN = "5750208451:AAEKOMdAug0pbDaL4D2t9Mb6TRm5ueKRmiM"
ADMINS = [719450837]

def pulling():
    count_message = 0
    while True:
        response = requests.get(f'{BASE_URL}{TOKEN}/getUpdates').json()
        if count_message != len(response['result']):
            count_message = len(response['result'])
            message = response['result'][-1]
            file_id = message['message']['voice']['file_id']
            user_id = message['message']['from']['id']
            if user_id in ADMINS:
                requests.get(f'{BASE_URL}{TOKEN}/sendVoice?chat_id={user_id}&voice={file_id}')


pulling()
