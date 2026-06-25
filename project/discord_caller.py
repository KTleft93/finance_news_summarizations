import requests
from dotenv import load_dotenv
import os

load_dotenv()

WEBHOOK_URL = (os.getenv("DISCORD_URL"))


def send_discord_message(content):
    # Discord limits messages to 2000 characters
    if len(content) > 2000:
        content = content[:1997] + "..."

    data = {"content": content}
    response = requests.post(WEBHOOK_URL, json=data)

    if response.status_code != 204:
        print(f"Failed to send: {response.status_code} {response.text}")
    else:
        print("Sent to Discord!")


send_discord_message("NEWS ARTICLE OUTPUT HEADER")