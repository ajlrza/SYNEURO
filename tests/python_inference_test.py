import os, sys, unittest
import unittest
from dotenv import load_dotenv

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)


class TestInference(unittest.TestCase):

    def test_init_syneuro_conscious_state(self):
        
        app_output = {
            'sensory': {
                '2026-06-25T12:30:00.000Z': 'I AM MADD.',
                '2026-06-25T1:30:00.000Z': 'IM SO HAPPY',
            },
            'modalities': [
                'Text',
                'Text'
            ],
            'request_activation': [
                'CEN',
                'LIM'
            ],
            'active_modules': [
                'CEN',
                'LIM'
            ],
        }

        load_dotenv()
        api_key = os.getenv('TEST_CASE_KEY')
        from services.python_inference.inference.brain import Brain
        brain = Brain(app_output, api_key)

        from services.python_inference.inference.brain import syneuro_conscious_state
        syneuro_conscious_state(Brain, app_output, api_key)


    def test_activate_bm_syneuro(self):

        app_output = {
            'sensory': {
                '2026-06-25T12:30:00.000Z': 'This is a test yay.',
                '2026-06-25T1:30:00.000Z': 'This is not a test!!!',
            },
            'modalities': [
                'Text',
                'Text'
            ],
            'request_activation': [
                'CEN',
                'CLIM'
            ],
            'active_modules': [
                'CEN',
                'LIM'
            ],
        }

        load_dotenv()
        api_key = os.getenv('TEST_CASE_KEY')
        from services.python_inference.inference.brain import Brain
        brain = Brain(app_output, api_key)
        
        activate_bm = brain.activate_brain_module('LIM')
        from services.python_inference.inference.networks.network_imports import network_builder  

        lim = network_builder("LIM")

        active_modules_equality = {
            'LIM': lim(app_output, api_key)
        }

        if (activate_bm):
            return_type = type(activate_bm)
            self.assertEqual(return_type, str)

        self.assertIsInstance(brain.active_modules['LIM'], type(active_modules_equality['LIM']))




