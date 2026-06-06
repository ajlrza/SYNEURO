import os
import json
import subprocess
from openai import OpenAI
from groq import Groq
from dotenv import load_dotenv

class agentManager:
      user = ""
      message = ""
      state = False
      tokens_used = 0

      def __init__(self, user):
          self.user = user
          self.state = True
          self.tokens_used = 0

      def startApp(self):
           if (self.state != True):
               # Sometimes the start app may be called without init
               return "Instance required, failed to start app"
           
           if (self.state == True):
                # This will start a while loop to initiate
                # A continuous chat event with Kurisu
                print("Initiliazing application...")
                self.state == True
                return self.state

      def stopApp(self):
           if (self.state == True):
                self.state = False
                return True
           
      def monitorApp(self, choice):
           if (choice == "User"):
                return self.user
           elif (choice == "State"):
                return self.state
           
      def chatGroq(self, client, user, sys_prompt_lore, sys_prompt_background, message: str):
          message_response = {}
          if (message != None):
               chat_groq = client.chat.completions.create(
                    messages=[
                         {
                              "role": "user",
                              "content": message,
                         }
                    ],
                    model="llama-3.3-70b-versatile"
               )
               client_usage_monitor = {
                    "Completion Time": chat_groq.usage.completion_time,
                    "Tokens Used": chat_groq.usage.completion_tokens,
                    "Completion Details": chat_groq.usage.completion_tokens_details
               }
               message_response["Response"] = chat_groq.choices[0].message.content
               self.tokens_used += client_usage_monitor["Tokens Used"]
               if (self.tokens_used > 3000 and self.tokens_used < 6000):
                    message_response["Tokens Used"] = self.tokens_used
               return message_response
          else:
               return "Message cannot be empty."
          
class agentBrain:
     # Configure the brain
     DFM = DFMNetwork()
     CEN = CENetwork()
     SAL = SALNetwork()
     SEN = SENNetwork()
     VIS = VISNetwork()
     LIM = LIMNetwork()
     VEN = VENNetwork()

load_dotenv() 

client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)

def appProxy(dataObject: object):

    # Inside the object
    UserID = dataObject["UserID"]
    Message = dataObject["Message"]
    Date = dataObject["Date"]
    Time = dataObject["Time"]
    Waifu = dataObject["Waifu"]
    ConversationID = dataObject["ConversationID"]

    # Start db listener
    dbListener = subprocess.run(["npx", "ts-node", "database_communication/db_server.ts"])

    # Write to JSON
    with open("bridge.json", "r") as file:
        data = json.load(file)
    data["Communication"]["Object"] = dataObject
    data["Communication"]["Written"] = True
    with open("bridge.json", "w") as file:
        json.dump(data, file, indent=4)

    # Check JSON
    with open("bridge.json", "r") as file:
        data = json.load(file)
        #soon

    groq_app = agent_classes.agentManager(UserID)
    
    # Change soon

    talk_to_groq = groq_app.chatGroq(client, UserID, sys_prompt.kurisu_personality_prompt("Lore"), sys_prompt.kurisu_personality_prompt("Personality"), message)
    
    return talk_to_groq

        
