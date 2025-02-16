import os
import logging
from twilio.rest import Client
from dotenv import load_dotenv

# Configure logging
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

def get_twilio_client():
    """Initialize Twilio client with environment variables"""
    try:
        account_sid = os.environ["TWILIO_ACCOUNT_SID"]
        auth_token = os.environ["TWILIO_AUTH_TOKEN"]
        return Client(account_sid, auth_token)
    except KeyError as e:
        logger.error(f"Missing Twilio credentials: {e}")
        raise
    except Exception as e:
        logger.error(f"Failed to initialize Twilio client: {e}")
        raise

def send_notification():
    """Send phone call notification using Twilio"""
    try:
        client = get_twilio_client()
        to_number = os.environ.get("TWILIO_TO_NUMBER")
        from_number = os.environ.get("TWILIO_FROM_NUMBER")
        
        if not all([to_number, from_number]):
            raise ValueError("Missing phone number configuration")

        call = client.calls.create(
            to=to_number,
            from_=from_number,
            url="http://demo.twilio.com/docs/voice.xml",
        )
        logger.info(f"Notification call initiated: {call.sid}")
        return call.sid
    except Exception as e:
        logger.error(f"Failed to send notification: {e}")
        raise