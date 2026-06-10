from network_imports import networkBuilder
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


    def __filterModalities(self, modalities_list: list) -> bool:
        accepted_modalities = {"Text", "Audio", "Video", "Image", "VideoSensor"} 

        valid_count = sum(1 for m in modalities_list if m in accepted_modalities)
        
        return valid_count >= 1

    def __handleTextOutput(self, userText: str) -> dict:
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
    
    async def pushAttention(attentionList: list, taskCount: int):
        for attention in attentionList:
            workingMemory.append(attention)
            # Metadata to track how many attention is being held in working memory
            workingMemory.count(1)
        # For networks to know
        return workingMemory
