import os
import json
import subprocess
from networks.network_imports import network_builder
from openai import OpenAI
from groq import Groq
from dotenv import load_dotenv
         
class Brain:
     # Configure the brain
     DFMBuild = network_builder("DFM")
     CENBuild = network_builder("CEN")
     SALBuild = network_builder("SAL")
     SENBuild = network_builder("SEN")
     VISBuild = network_builder("VIS")
     LIMBuild = network_builder("LIM")
     VENBuild = network_builder("VEN")

     DFM = DFMBuild()
     CEN = CENBuild()
     SAL = SALBuild()
     SEN = SENBuild()
     VIS = VISBuild()
     LIM = LIMBuild()
     VEN = VENBuild()

     task_count = 0
     app_output = {}

     def __init__(self, app_output: object):
         self.app_output = app_output
         if 'tasks' in app_output:
          self.task_count = len(app_output['tasks'])
         
     async def track_attention(self):
         task_attentions = list(self.app_output['tasks'].values())
         track_attention = await self.CEN.push_attention(task_attentions, self.task_count)
         return track_attention


load_dotenv() 

client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)

async def syneuro_inference(app_output: object):
    brain_management = Brain(app_output)
    tracked_attention = brain_management.track_attention()
    


        
