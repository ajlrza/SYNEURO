class agentManager:
      user = ""
      message = ""
      state = False
      tokens_used = 0

      def __init__(self, user):
          self.user = user
          self.state = True
          self.tokens_used = 0

      def startApp(self):
           if (self.state != True):
               # Sometimes the start app may be called without init
               return "Instance required, failed to start app"
           
           if (self.state == True):
                # This will start a while loop to initiate
                # A continuous chat event with Kurisu
                print("Initiliazing application...")
                self.state == True
                return self.state

      def stopApp(self):
           if (self.state == True):
                self.state = False
                return True
           
      def monitorApp(self, choice):
           if (choice == "User"):
                return self.user
           elif (choice == "State"):
                return self.state
           
      def chatGroq(self, client, user, sys_prompt_lore, sys_prompt_background, message: str):
          message_response = {}
          if (message != None):
               chat_groq = client.chat.completions.create(
                    messages=[
                         {
                              "role": "user",
                              "content": message,
                         }
                    ],
                    model="llama-3.3-70b-versatile"
               )
               client_usage_monitor = {
                    "Completion Time": chat_groq.usage.completion_time,
                    "Tokens Used": chat_groq.usage.completion_tokens,
                    "Completion Details": chat_groq.usage.completion_tokens_details
               }
               message_response["Response"] = chat_groq.choices[0].message.content
               self.tokens_used += client_usage_monitor["Tokens Used"]
               if (self.tokens_used > 3000 and self.tokens_used < 6000):
                    message_response["Tokens Used"] = self.tokens_used
               return message_response
          else:
               return "Message cannot be empty."

# Default mode network of the agent brain
class DFMNetwork:
     def __init__(self, agentOutput):
          pass
# Executive function
class CENetwork:
     def __init__(self, agentOutput):
          pass
# Manages DFM and CEN
class SALNetwork:
     def __init__(self, DFMCENObject):
          pass
# Sensorimotor function
class SENNetwork:
     # Responsible for communication processing
     def __init__(self, agentOutput, userOutput):
          pass
class VISNetwork:
     def __init__(self):
          pass
class LIMNetwork:
     # Responsible for  Deeply involved in the emotional center of the brain; it regulates mood, emotional responses, motivation, and memory formation.
     def __init__(self, agentOutput, userOutput):
          self.Happy = 0
          self.Sad = 0
          self.Disgust = 0
          self.Fear = 0
          self.Anger = 0
          self.Surprise = 0
          pass
     # The Thalamo-Amygdala Pathway

     # Since there are 100feeelings, itsmost likely 
class VENNetwork:
     # Unexpected attention awareness, randomness
     def __init__(self):
          pass

# Brain - orchestrates each class (brain parts)
# Though I may change the architecture if it scales up
class agentBrain:
     # Configure the brain
     DFM = DFMNetwork()
     CEN = CENetwork()
     SAL = SALNetwork()
     SEN = SENNetwork()
     VIS = VISNetwork()
     LIM = LIMNetwork()
     VEN = VENNetwork()
     pass
