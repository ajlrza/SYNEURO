import contextRAG
import CENNetwork

class SALNetwork:
     RAG
     environmentalData = []
     attentionList = []
     currentAttention = {}
     
     def __init__(self, rawData: any):
          self.environmentalData.append(rawData)
          # Get current status of user activity

     def signalNetwork(self) -> None:
          RAG = contextRAG(self.environmentalData)
          for state, data in enumerate(RAG):
               if (state == "Focus"):
                    self.attentionList.append(data)
                    
     def divertAttention(self):
          attentionCount = 0
          taskCount = 0
          CEN = CENNetwork()
          
          for attention in self.attentionList:
               attentionCount += 1
               currentAttention[attentionCount] = attention
               
          while (True):
               CEN.pushAttention(self.attentionList[taskCount]
               if (self.RAG.workingMemory() <= 100):
                  self.RAG.addMemory(attentionList[taskCount - 1]
               if (CEN.checkAttention == False):
                   continue
               else:
               # Note: Attention is the data from user, should SLM be involved here hm
                  if (self.RAG.workingMemory() != "Full"): 
                     self.RAG.addMemory(attentionList[taskCount])
                     attentionList.pop(taskCount)
                     taskCount += 1
                  else:
                     self.RAG.addTempMemory(attentionList[taskCount]
                     attentionList.pop(taskCount)
                     taskCount += 1
               
               
