# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

def call():
    call = client.calls.create(
        to=os.environ.get("TWILIO_TO_NUMBER"),
        from_=os.environ.get("TWILIO_FROM_NUMBER"),
        url="http://demo.twilio.com/docs/voice.xml",
    )
    print(call.sid)

if __name__ == '__main__':
    call()