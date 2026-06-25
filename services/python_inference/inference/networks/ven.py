class VENNetwork:
     # Unexpected attention awareness, randomness
     salOutput: dict
     agentOutput: any

     def __init__(self, salOutput, agentOutput):
          self.salOutput = salOutput
          self.agentOutput = agentOutput

     def change_current_attention(self, attention: int, attention_weight: int):
         current_attention = self.salOutput.workingMemory.get(self.salOutput[attention])
         new_attention = self.salOutput.workingMemory.get(self.salOutput[attention * attention_weight])
         return new_attention

#In a biological brain, the VEN is triggered by raw, bottom-up sensory input. 
# A sudden flash in your peripheral vision (Visual Network) or a sudden tap on your shoulder 
# (Sensorimotor Network) forces the VEN to interrupt the system before the Salience network 
# has fully categorized it.

# In our case, through user webcam or text? it can react?