import os
import json
import time
import asyncio
import numpy as np
from network_imports import networkBuilder 
from groq import Groq
from enum import Enum

CENClass = networkBuilder("CEN")
CEN = CENClass()

class sensoryOutput:
     Text: str = ""
     Audio: bytearray
     Video: bytearray # or ndarray? bytearray is temp

class bloch:
     blochVector: np.array = ([[[]]])
     x = np.linspace(0, 30, 45, 60, 90)
     y = np.linspace(0, 30, 45, 60, 90)
     z = np.linspace(0, 30, 45, 60, 90)
     coords: list

     '''
     Z-axis - emotional intensity
     X, Y axis - affective states
     '''

     def __init__(self):
          self.X, self.Y, self.Z = np.meshgrid(self.x, self.y, self.z, indexing="ij")
          self.coords = np.stack((self.X, self.Y, self.Z), axis=1)
          pass

     def check_normalization(self) -> bool:
          if (abs(self.ketA) + abs(self.ketB) == 1):
               return True

     def compute_bloch_sphere(self, x: float, y: float, z: float):
          # should it be able to track previous bloch sphre values?
          pass

     # need quantum logic gates soon, refactor everything, and re-logi

          
angles = {
     0: np.radians(0),
     30: np.radians(30),
     45: np.radians(45),
     60: np.radians(60),
     90: np.radians(90)
}

def get_emotional_state(degree: int) -> float:
     if degree not in angles:
          raise ValueError("Degree not found.")
     
     xi = angles[degree]

     amp_0: float = np.cos(xi)
     amp_1: float  = np.sin(xi)

     return amp_0, amp_1

class quantumEmotion:
     emotionalState: float
     affectiveState: dict
     blochVector: np.array = ([[[]]])

     def __init__(self, affectiveState: dict):
          self.affectiveState = affectiveState

     def compute_emotion_superposition(self, amp_0, amp_1) -> np.complex128:
          cdtype = np.complex128
          ket_0 = np.array([[1],
                         [0]], dtype=cdtype)
          ket_1 = np.array([[0],
                         [1]], dtype=cdtype)
          quantumEmotion = (amp_0 * ket_0) + (amp_1 * ket_1)
          return quantumEmotion

     def compute_emotion_transition(self, stimulus, emotionState):
          # Make sure matrix is unitary
          transitionState = stimulus * emotionState
          #how inverse?
          pass

     def compute_emotion_state():
          pass

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
     agentEmotion = quantumEmotion()

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
     def thalamus(self, sensoryData: dict):

          def check_attention(saved_state_vector, last_timestamp, decay_rate):
               attentionDecay = CEN.attentionCheck(saved_state_vector, timestamp, decay_rate)
               if (attentionDecay):
                    return attentionDecay
               else:
                    return False

          # Emotional stimulus processing
          for timestamp, sensorData in sensoryData.items:
               match type(sensorData).__name__:
                    # might need to scale, could we handle tons of data, or for MVP, this one would do?
                    
                    # ASYNCIO FOR DATA FLOW, NETWORKING, AND COMMUNICATION
                    # MULTIPROCESSING MODULE FOR MATRIX, MATH, AND OPTMIZE, ANYTHING IN NUMPY, NN

                    case "str":
                         sensoryOutput.Text = sensorData
                         self.amygdala(sensoryOutput.Text)
                         attentionGate = check_attention(self.saved_state_vector, timestamp, self.decay_rate)
                         asyncio.create_task(CEN.push_attention(attentionGate, sensorData))
                    case "bytearray":
                         # sensoryOutput is a class because the brain will also check it, be used in other areas
                         sensoryOutput.Audio = sensorData
                         self.amygdala(sensoryOutput.Audio)
                         attentionGate = check_attention(self.saved_state_vector, timestamp, self.decay_rate)
                         asyncio.create_task(CEN.push_attention(attentionGate, sensorData))
                    case "ndarray":
                         sensoryOutput.Video = sensorData
                         self.amygdala(sensoryOutput.Video)
                         attentionGate = check_attention(self.saved_state_vector, timestamp, self.decay_rate)
                         asyncio.create_task(CEN.push_attention(attentionGate, sensorData))
          
          # Memory formation
          check_emotion_states = self.agentEmotion.affectiveState
          # Runs in background
          # If working memory and current emotion are linked
          # through high stimulus
          # It becomes long-term memory
          # will refactor soon
          form_long_term_memories = asyncio.create_task([CEN.get_working_memory() ** stimulus for stimulus in
          check_emotion_states.items if stimulus > self.saved_state_vector])

                    
     def amygdala(self, emotionalStimulus: any):
          #background? 
          extractAffectiveState = self.extract_affective_state(emotionalStimulus)
          pass
                    
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