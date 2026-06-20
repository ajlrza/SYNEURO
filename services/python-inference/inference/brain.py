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

     app_output = {}

     def __init__(self, app_output: object):
         self.app_output = app_output

async def syneuro_inference(app_output: object, api_key: str):
    brain_management = Brain(app_output)

    tracked_attention = brain_management.track_attention()
    init_emotion = brain_management.LIM(brain_management.app_output, api_key)
    process_emotion_stimulus = brain_management.LIM.amygdala()
    


        
