import unittest
from dotenv import load_dotenv
from services.python_inference.inference.brain import *
from services.python_inference.inference.networks.network_imports import *

class TestInference(unittest.TestCase):

    def test_init_syneuro_conscious_state(self):
        
        app_output = {
            'sensory': {
                '2026-06-25T12:30:00.000Z': 'This is a test yay.',
                '2026-06-25T1:30:00.000Z': 'This is not a test!!!',
            },
            'modalities': {
                'Text',
                'Text'
            },
            'active_modules': [
                'CEN',
                'LIM'
            ],
        }

        load_dotenv()
        api_key = os.getenv('TEST_CASE_KEY')
        brain = Brain(app_output, api_key)

        self.assertIsInstance(brain, Brain)

    def test_activate_bm_syneuro(self):

        app_output = {
            'sensory': {
                '2026-06-25T12:30:00.000Z': 'This is a test yay.',
                '2026-06-25T1:30:00.000Z': 'This is not a test!!!',
            },
            'modalities': {
                'Text',
                'Text'
            },
            'active_modules': [
                'CEN',
                'LIM'
            ],
        }

        load_dotenv()
        api_key = os.getenv('TEST_CASE_KEY')
        brain = Brain(app_output, api_key)
        
        activate_bm = brain.active_modules('LIM')
        active_modules_equality = {
            'LIM': LIMNetwork()
        }

        if (activate_bm):
            return_type = type(activate_bm)
            self.assertEqual(return_type, str)

        self.assertDictEqual(brain.active_modules, active_modules_equality)



