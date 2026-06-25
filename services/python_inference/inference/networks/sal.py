from network_imports import network_builder 
import RAG


class SALNetwork:
     cen_class = network_builder("CEN")
     cen = cen_class()
     RAG: RAG.instance
     environmental_data = []
     attention_list = []
     current_attention = {}
     
     def __init__(self, raw_data: any):
          self.environmental_data.append(raw_data)
          # Get current status of user activity

     def signal_network(self) -> None:
          RAG = self.RAG.context_rag(self.environmental_data)
          for state, data in enumerate(self.RAG.current_context):
               if (state == "Focus"):
                    self.attention_list.append(data)
                    
     def divert_attention(self):
          attention_count = 0
          task_count = 0
          
          for attention in self.attention_list:
               attention_count += 1
               self.current_attention[attention_count] = attention
               
          while (True):
               if (self.RAG.working_memory() <= 100):
                  self.RAG.add_memory(self.attention_list[task_count - 1])
               elif (cen.check_attention == False):
                   continue
               else:
               # Note: Attention is the data from user, should SLM be involved here hm
                  if (self.RAG.working_memory() != "Full"): 
                     self.RAG.add_memory(self.attention_list[task_count])
                     self.attention_list.pop(task_count)
                     task_count += 1
                  else:
                     self.RAG.add_temp_memory(self.attention_list[task_count])
                     self.attention_list.pop(taskCount)
                     taskCount += 1
               
     async def store_attention(self, attentionList: list, taskCount):
          attentionList = attentionList
          await add_attention = self.cen.push_attention(self.attentionList, taskCount)
          return add_attention
     
               
