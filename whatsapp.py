# whatsapp.py

import re
import requests

# UltraMsg API Credentials
ULTRAMSG_INSTANCE_ID = "instance133731"
ULTRAMSG_TOKEN = "vmpy068dk84a9wyx"
ULTRAMSG_BASE_URL = f"https://api.ultramsg.com/{ULTRAMSG_INSTANCE_ID}/messages/chat?token={ULTRAMSG_TOKEN}"

# --- Format any phone number to 92XXXXXXXXXX ---
def format_number(input_number):
    cleaned = re.sub(r'\D', '', input_number)
    if cleaned.startswith('92') and len(cleaned) == 12:
        return cleaned
    elif cleaned.startswith('03') and len(cleaned) == 11:
        return '92' + cleaned[1:]
    elif cleaned.startswith('+92') and len(cleaned) == 13:
        return cleaned[1:]
    elif len(cleaned) == 10:
        return '92' + cleaned
    else:
        return None

# --- Send WhatsApp message ---
def send_whatsapp_message(to_number, message):
    payload = {
        "to": to_number,
        "body": message,
    }
    response = requests.post(ULTRAMSG_BASE_URL, data=payload)
    return response.json()
