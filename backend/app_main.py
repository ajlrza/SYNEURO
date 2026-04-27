from openai import OpenAI
from groq import Groq
import os
import os
from . import sys_prompt
from . import classes
from dotenv import load_dotenv

load_dotenv() 

client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)

groq_app = classes.appManager()

        
