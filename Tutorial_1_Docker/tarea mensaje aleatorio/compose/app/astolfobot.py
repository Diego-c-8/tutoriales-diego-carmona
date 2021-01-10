import os

from pymongo import MongoClient

# Create the JamesBot Class
class AstolfoBot:

    # Create a constant that contains the default texts for the message
    YAHALLO = [
        {
            "dict":{
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "yahooo soy astolfo!"
                }
            }

        },{
            "dict":{
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "yahallo i am astolfo!"
                }
            }

        },{
            "dict":{
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "YAHALLOOOOOO BOKU WA ASTOLFO DES!"
                }
            }

        }
    ]

    
    # The constructor for the class.
    def __init__(self, channel):
        self.channel = channel
        self.client = MongoClient(os.environ.get("MONGO_PORT"))
        self.db = self.client.yahallo
        self.yahallo = self.db.yahallo
        self.yahallo.insert_many(self.YAHALLO)

    
    #Get random message from db
    def _choose_message(self):
        return self.yahallo.aggregate([{ "$sample": {"size": 1} }]).next()["dict"]
    

    # Craft and return the entire message payload as a dictionary.
    def get_message_payload(self):
        return {
            "channel": self.channel,
            "blocks": [
                self._choose_message()
            ]
        }
