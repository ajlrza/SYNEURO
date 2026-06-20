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
     pass

def get_emotional_state(valence: float, arousal: float) -> tuple[np.complex128, np.complex128]:
    """
    Translates continuous VAD metrics into 3D quantum probability amplitudes.
    Valence (-1.0 to 1.0) drives the polar angle (Theta).
    Arousal (-1.0 to 1.0) drives the azimuthal phase (Phi).
    """
    theta = np.interp(valence, [-1.0, 1.0], [np.pi, 0])      
    phi = np.interp(arousal, [-1.0, 1.0], [0, 2 * np.pi])    

    amp_0 = np.cos(theta / 2)
    
    amp_1 = np.exp(1j * phi) * np.sin(theta / 2)

    return amp_0, amp_1

class quantumEmotion:
     emotional_state: float
     affective_state: np.ndarray
     stimulus_states: dict
     state_vector: np.array
     bloch_vector: np.array = ([[[]]])

     def __init__(self):
        self.state_vector = np.array([[1.0 + 0.j], [0.0 + 0.j]], dtype=np.complex128)

     def map_vad_to_angles(self, valence, arousal):
        theta = np.interp(valence, [-1, 1], [np.pi, 0])
        phi = np.interp(arousal, [-1, 1], [0, 2 * np.pi])
        return theta, phi
     
     def compute_emotion_state(self, valence, arousal, dominance):
        theta, phi = self.map_vad_to_angles(valence, arousal)
        
        amp_0 = np.cos(theta / 2)
        amp_1 = np.exp(1j * phi) * np.sin(theta / 2)
        
        self.state_vector = dominance * np.array([[amp_0], [amp_1]], dtype=np.complex128)
        return self.state_vector
     
     def compute_emotion_transition(self, stimulus_vad):
        theta, phi = self.map_vad_to_angles(stimulus_vad['valence'], stimulus_vad['arousal'])
        
        U = np.array([
            [np.cos(theta/2), -np.exp(-1j*phi) * np.sin(theta/2)],
            [np.exp(1j*phi) * np.sin(theta/2), np.cos(theta/2)]
        ], dtype=np.complex128)
        
        self.state_vector = np.dot(U, self.state_vector)
        self.affective_state = self.state_vector
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
     sensor: sensoryOutput
     emotion: quantumEmotion
     emotionDict: dict 

     # Responsible for  Deeply involved in the emotional center of the brain; it regulates mood, emotional responses, motivation, and memory formation.
     def __init__(self, appOutput: dict, apiKey: str):
          self.client = Groq(api_key=apiKey)
          self.sensor = sensoryOutput()
          self.emotion = quantumEmotion()
          self.emotionDict = {
          "Happy": 0,
          "Sad": 0,
          "Disgust": 0,
          "Fear": 0,
          "Anger": 0,
          "Surprise": 0,
          }
          self.thalamus(appOutput)

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
                         attentionGate = check_attention(self.emotion.state_vector, timestamp, 2.0) #test self.decayrate
                         asyncio.create_task(CEN.push_attention(attentionGate, sensorData))
                    case "bytearray":
                         # sensoryOutput is a class because the brain will also check it, be used in other areas
                         sensoryOutput.Audio = sensorData
                         self.amygdala(sensoryOutput.Audio) 
                         attentionGate = check_attention(self.emotion.state_vector, timestamp, 3.0)#test self.decayrate
                         asyncio.create_task(CEN.push_attention(attentionGate, sensorData))
                    case "ndarray":
                         sensoryOutput.Video = sensorData
                         self.amygdala(sensoryOutput.Video)
                         attentionGate = check_attention(self.emotion.state_vector, timestamp, 4.0)#test self.decayrate
                         asyncio.create_task(CEN.push_attention(attentionGate, sensorData))
                    
     async def amygdala(self, emotionalStimulus: any):
          amygdala_work = set()

          # Stimulated brain
          get_vad = self.extract_affective_state(emotionalStimulus)
          map_result = self.emotion.map_vad_to_angles(get_vad)
          compute_emotion = self.emotion.compute_emotion_state(map_result)

          # Emotional transition from current sensory data
          # Check if sensory data are not empty
          if (self.sensor.Text != '' or self.sensor.Audio != bytearray() or self.sensor.Video != bytearray()):
               # Yet, emotional state is not intense
               if (self.emotion.emotional_state <= 0):
                    transition_the_emotion = asyncio.create_task(
                         self.emotion.compute_emotion_transition(self.emotion.affective_state)
                    )
                    amygdala_work.add(transition_the_emotion)
               # Emotional state is high, will transition to calm
               elif (self.emotion.emotional_state >= 0 and self.emotion.affective_state['Valence'] >= 0 and
                     self.emotion.affective_state['Arousal'] <= 0):
                    transition_the_emotion = asyncio.create_task(
                         self.emotion.compute_emotion_transition(self.emotion.affective_state)
                    )
                    amygdala_work.add(transition_the_emotion)

          # Memory formation
          # Runs in background
          # If working memory and current emotion are linked
          # through high stimulus
          # It becomes long-term memory
          # will refactor soon
          check_stimulus_states = self.emotion.stimulus_states
          form_long_term_memories = asyncio.create_task([CEN.get_working_memory() ** stimulus for stimulus, state in
          check_stimulus_states.items() if state > self.emotional_state])
          amygdala_work.add(form_long_term_memories)
          pass
                    
     def extract_affective_state(self, app_output: dict) -> np.ndarray:
   
          system_prompt = """
          You are a sensory feature extractor. Analyze the data and output ONLY valid JSON.
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