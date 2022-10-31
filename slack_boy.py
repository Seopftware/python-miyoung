import requests
import json

def send_slack_message():
    slack_url = "https://hooks.slack.com/services/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"
    message = """
    여러분 화이팅!
    """ 

    payloads = {
        "text": message,
    }

    response = requests.post(
        slack_url, data=json.dumps(payloads),
        headers={'Content-Type': 'application/json'}
    )
    
    print(response)
        
send_slack_message()