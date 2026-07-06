import os
import sys
import subprocess
from groq import Groq

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from services.python_inference.inference.networks.network_imports import network_builder


class Brain:
     # Configure the brain
     active_modules = {}
     api_key: str
     app_output = {}

     def __init__(self, app_output: object, api_key):
         self.app_output = app_output
         self.api_key = api_key

     def activate_brain_module(self, brain_module: str):
         if brain_module in self.active_modules.keys():
            return f'{brain_module} is already active.'
         
         try:   
            self.active_modules[brain_module] = network_builder(brain_module)
         except:
            self.active_modules[brain_module] = network_builder(brain_module)
        
def syneuro_conscious_state(brain: Brain, app_output: object, api_key: str):
    brain_management = brain(app_output, api_key)

    if (len(app_output['request_activation']) >= 1):
        for brain_module in app_output['request_activation']:
            brain_management.activate_brain_module(brain_module)

    if (len(app_output['sensory'].keys()) >= 1 and len(brain_management.active_modules.keys()) >= 1):
        # Assume CEN and LIM are always activated or thismight berisky?
        cen_work = brain_management.active_modules['CEN']
        lim_work = brain_management.active_modules['LIM']
        cen_active = cen_work(app_output)
        lim = lim_work(app_output, api_key)
        print(lim.emotion_matrix)
    else:
        return ("Syneuro does not process any sensor_data and active brain modules at the moment.")
    
    # There's no need for database ID in this, as it is not an application but a middleware.



        
