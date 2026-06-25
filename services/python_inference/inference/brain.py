import os
import json
import subprocess
from networks.network_imports import network_builder
from groq import Groq

         
class Brain:
     # Configure the brain
     active_modules: dict

     app_output = {}

     def __init__(self, app_output: object):
         self.app_output = app_output
         self.active_modules = {}

     def activate_brain_module(self, brain_module: str):
         if brain_module in self.active_modules:
            return f'{brain_module} is already active.'
         
         self.active_modules[brain_module] = network_builder(brain_module)()
        
def syneuro_conscious_state(app_output: object, api_key: str):
    brain_management = Brain(app_output)

    if (len(app_output.request_activation) >= 1):
        for brain_module in app_output.request_activation:
            brain_management.activate_brain_module(brain_module)

    if (app_output.sensor_data >= 1 and brain_management.active_modules.keys >= 1):
        # Assume CEN and LIM are always activated or thismight berisky?
        cen_work = brain_management.active_modules['CEN']
        lim_work = brain_management.active_modules['LIM']
        try:
            cen_active = cen_work(app_output)
        except ValueError as E:
            return E
        lim_emotion = lim_work(app_output)

        return lim_emotion

    else:
        return "Syneuro does not process any sensor_data and active brain modules at the moment."
    
    # There's no need for database ID in this, as it is not an application but a middleware.



        
