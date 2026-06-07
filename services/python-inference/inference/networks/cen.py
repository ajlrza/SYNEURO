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
    # Class hint
    agentOutput: any

    def __init__(self, agentOutput: object):
        # Assuming agentOutput.Modalities is a LIST like ["Text", "Video"]
        # Check if we have at least 2 modalities (length of the list)
        if len(agentOutput.Modalities) >= 2:
            
            if self.__filterModalities(agentOutput.Modalities):
                self.agentOutput = agentOutput
            else:
                raise ValueError("Modality not accepted. Only accepts Text, Audio, Video, Image, or VideoSensor.")
        else:
            raise ValueError("CENetwork requires at least 2 modalities.")

    # Made this a private method inside the class
    def __filterModalities(self, modalities_list: list) -> bool:
        accepted_modalities = {"Text", "Audio", "Video", "Image", "VideoSensor"} # Using a set is faster
        
        # Check if ANY of the incoming modalities match our accepted set
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
        # Logic to merge visual_spikes and text_spikes would go here
        return fused_state
