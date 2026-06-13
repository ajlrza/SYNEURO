from network_imports import networkBuilder
import time
import numpy as np
import workingMemory

# Executive function
def filterModalities(Modalities: object):
     acceptedModalities = [
          "Text", 
          "Audio", 
          "Video",
          "Image",
          "VideoSensor"
          ]
     filteredModalities = []

     for modality in Modalities:
          if modality in acceptedModalities:
               filteredModalities.append(True)
     
     if filteredModalities >= 1:
          return True
     else:
          return False
     

class CENetwork:

    agentOutput: any

    def __init__(self, agentOutput: object):
 
        if len(agentOutput.Modalities) >= 2:
            
            if self.__filterModalities(agentOutput.Modalities):
                self.agentOutput = agentOutput
            else:
                raise ValueError("Modality not accepted. Only accepts Text, Audio, Video, Image, or VideoSensor.")
        else:
            raise ValueError("CENetwork requires at least 2 modalities.")


    def __filter_modalities(self, modalities_list: list) -> bool:
        accepted_modalities = {"Text", "Audio", "Video", "Image", "VideoSensor"} 

        valid_count = sum(1 for m in modalities_list if m in accepted_modalities)
        
        return valid_count >= 1

    def __handle_text_output(self, userText: str) -> dict:
        Spike = False
        TRE_Neurons = {}
        
        if userText:
            Spike = True
            for count, text_char in enumerate(userText, start=1):
                neuron_name = f"Neuron {count}"
                if neuron_name not in TRE_Neurons:
                    TRE_Neurons[neuron_name] = 0
                
                TRE_Neurons[neuron_name] += 1 * len(userText)

        return TRE_Neurons 

    def PPC(self, visual_spikes: dict, text_spikes: dict) -> dict:
        """
        Posterior Parietal Cortex layer.
        Fuses multimodal spike trains before the Central Executive reasons over them.
        """
        fused_state = {}

        return fused_state
    
    async def push_attention(attentionList: list, taskCount: int):
        for attention in attentionList:
            workingMemory.append(attention)
            # Metadata to track how many attention is being held in working memory
            workingMemory.count(1)
        # For networks to know
        return workingMemory
    
    def attention_check(self, saved_state_vector: np.array, last_timestamp: time, decay_rate: float):
        """
        Applies exponential decay to the emotional vector based on elapsed time.
        Brings extreme emotions back toward 0 (Neutral).
        """
        current_time = time.time()
        time_delta_seconds = current_time - last_timestamp
        decay_factor = 0

        if (time_delta_seconds < current_time and decay_rate >= 1.0): 
            pass

            #approaches 0
        if (time_delta_seconds > current_time and decay_rate <= 0): 
            self.decay_factor = np.exp(-decay_rate * time_delta_seconds)

        decayed_state = saved_state_vector * decay_factor
        return decayed_state


