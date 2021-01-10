from slack import WebClient
from jamesbot import JamesBot
import os

# Create a slack client
slack_web_client = WebClient(token=os.environ.get("SLACK_TOKEN"))

# Get a new CoinBot
james_bot = JamesBot("general")

# Get the onboarding message payload
message = james_bot.get_message_payload()

# Post the onboarding message in Slack
slack_web_client.chat_postMessage(**message)
