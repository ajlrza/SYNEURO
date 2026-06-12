import os
import json
import numpy as np
from network_imports import networkBuilder 
from groq import Groq
from enum import Enum

class sensoryOutput:
     Text: str = ""
     Audio: bytearray
     Video: bytearray # or ndarray? bytearray is temp

class emotionState:
     emotionalState: np.array = ([[]])
     affectiveState: dict

     def __init__(self, affectiveState: dict):
          self.affectiveState = affectiveState

     def quantumCompute(self):
          quantumStates: dict
          amplitudeA: int = 0
          amplitudeB: int = 0
          basisVectorA: np.array = [[1]]
          basisVectorB: np.array = [[0]]
          quantumEmotion = amplitudeA * basisVectorA + amplitudeB * basisVectorB

          #LOOP?
          #for state in self.affectiveState:
          # need pauli-Xgate operations
          # controlled rotation opeartion
          # emotion vector space
          #Emotion Fusion Complexity Formula

          # basically the output is the semantics from slm


class LIMNetwork:
     client: str
     sensoryOutput: any

     # Responsible for  Deeply involved in the emotional center of the brain; it regulates mood, emotional responses, motivation, and memory formation.
     def __init__(self, agentOutput, networksOutput):
          self.Happy = 0
          self.Sad = 0
          self.Disgust = 0
          self.Fear = 0
          self.Anger = 0
          self.Surprise = 0
          self.client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
          self.sensoryOutput = sensoryOutput()

     # The Thalamo-Amygdala Pathway
     def thalamoAmygdala(self, sensoryData: list):
          for data in sensoryData:
               match type(data).__name__:
                    # might need to scale, could we handle tons of data, or for MVP, this one would do?
                    case "str":
                         sensoryOutput.Text = data
                    case "bytearray":
                         sensoryOutput.Audio = data
                    case "np.array":
                         sensoryOutput.Video = data
          
          extractAffectiveState = self.extract_affective_state(sensoryOutput.Text)

                    
     def extract_affective_state(self, user_text: str) -> np.ndarray:
   
          system_prompt = """
          You are a sensory feature extractor. Analyze the text and output ONLY valid JSON.
          Format exactly like this: {"valence": float, "arousal": float, "dominance": float}
          Values must be between -1.0 and 1.0.
          """
     
          response = self.client.chat.completions.create(
               model="llama-3.1-8b-instant",
               messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_text}
               ],
               response_format={"type": "json_object"}, 
               temperature=0.1 
          )
          
          payload = json.loads(response.choices[0].message.content)
          e_stimulus = np.array([payload["valence"], payload["arousal"], payload["dominance"]])
          
          return e_stimulus


          # Since there are 100feeelings, itsmost likely 