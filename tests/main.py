import os
import sys

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from python_inference_test import *


def main():
    test = TestInference()
    test.test_init_syneuro_conscious_state()

if __name__ == "__main__":
    main()