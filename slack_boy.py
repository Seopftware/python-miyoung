import requests
import json

def send_slack_message():
    slack_url = "https://hooks.slack.com/services/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"
    message = """메세지 전송""" 

    payloads = {
        "text": message,
        "username": "수업 신청",
        "icon_emoji": ":clap:"
    }

    response = requests.post(
        slack_url, data=json.dumps(payloads),
        headers={'Content-Type': 'application/json'}
    )

    if response.status_code != 200:
        print("error" + response.status_code)