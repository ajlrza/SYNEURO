from network_imports import network_builder 

class SALNetwork:
     RAG
     environmentalData = []
     attentionList = []
     currentAttention = {}
     
     def __init__(self, rawData: any):
          self.environmentalData.append(rawData)
          # Get current status of user activity

     def signal_network(self) -> None:
          RAG = contextRAG(self.environmentalData)
          for state, data in enumerate(RAG):
               if (state == "Focus"):
                    self.attentionList.append(data)
                    
     def divert_attention(self):
          attentionCount = 0
          taskCount = 0
          CENBuild = network_builder("CEN")
          CEN = CENBuild(self.environmentalData)
          
          for attention in self.attentionList:
               attentionCount += 1
               self.currentAttention[attentionCount] = attention
               
          while (True):
               if (self.RAG.working_memory() <= 100):
                  self.RAG.addMemory(self.attentionList[taskCount - 1]
               if (CEN.checkAttention == False):
                   continue
               else:
               # Note: Attention is the data from user, should SLM be involved here hm
                  if (self.RAG.working_memory() != "Full"): 
                     self.RAG.add_memory(attentionList[taskCount])
                     attentionList.pop(taskCount)
                     taskCount += 1
                  else:
                     self.RAG.add_temp_memory(attentionList[taskCount]
                     attentionList.pop(taskCount)
                     taskCount += 1
               
     async def store_attention(self, attentionList: list, taskCount):
          attentionList = attentionList
          await addAttention = CEN.push_attention(self.attentionList, taskCount)
          return addAttention
     
               
