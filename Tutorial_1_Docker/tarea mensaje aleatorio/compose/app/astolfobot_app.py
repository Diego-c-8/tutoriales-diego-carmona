import os

from slack import WebClient
from astolfobot import AstolfoBot

# Initialize a Web API client
slack_web_client = WebClient(token=os.environ.get("SLACK_TOKEN"))

# Create a new JamesBot
astolfo_bot = AstolfoBot("general")

# Get the onboarding message payload
message = astolfo_bot.get_message_payload()

# Post the onboarding message in Slack
slack_web_client.chat_postMessage(**message)
