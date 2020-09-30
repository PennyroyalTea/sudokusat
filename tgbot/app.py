import os
import json

import requests


def lambda_handler(event, context):

    api_url = os.environ['SUDOKU_API_URL']
    bot_token = os.environ['BOT_TOKEN']

    body = event['body']
    message = json.loads(body)['message']

    chatId = message['chat']['id']
    text = message['text']

    result = requests.get(api_url, params={'data':text}).text

    requests.get('https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'.format(bot_token, chatId, result))

    return {
        "statusCode": 200,
        "body": json.dumps({
            "ok": "1"
        }),
    }
