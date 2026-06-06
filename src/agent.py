import os
import json
import subprocess
from openai import OpenAI
from groq import Groq
from .agent_communication import sys_prompt
from .agent_communication import agent_classes
from dotenv import load_dotenv


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

        
