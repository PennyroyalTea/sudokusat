import os
import json

import requests


def send_message(token, chat_id, message):
    requests.get('https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'.format(token, chat_id, message))


def lambda_handler(event, context):

    api_url = os.environ['SUDOKU_API_URL']
    bot_token = os.environ['BOT_TOKEN']

    body = event['body']
    message = json.loads(body)['message']

    chat_id = message['chat']['id']
    text = message['text']

    if text == '/start':
        send_message(bot_token, chat_id, 'Please, enter 81 digit (e.g. 530070000600195000098000060800060003400803001700020006060000280000419005000080079)')
        return {
            "statusCode": 200,
            "body": json.dumps({
                "ok": "1"
            }),
        }

    result = requests.get(api_url, params={'data':text}).text
    send_message(bot_token, chat_id, result)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "ok": "1"
        }),
    }
