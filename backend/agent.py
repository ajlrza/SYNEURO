from openai import OpenAI
from groq import Groq
import os
import os
from .agent_config import sys_prompt
from . import agent_classes
from dotenv import load_dotenv

load_dotenv() 

client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)

def appProxy(dataObject: object):

    UserID = dataObject["UserID"]
    Message = dataObject["Message"]
    Date = dataObject["Date"]
    Time = dataObject["Time"]
    Waifu = dataObject["Waifu"]
    ConversationID = dataObject["ConversationID"]

    # We need to talk to the database bruv

    groq_app = agent_classes.agentManager(UserID)
    
    # Change soon

    talk_to_groq = groq_app.chatGroq(client, UserID, sys_prompt.kurisu_personality_prompt("Lore"), sys_prompt.kurisu_personality_prompt("Personality"), message)
    
    return talk_to_groq

        
