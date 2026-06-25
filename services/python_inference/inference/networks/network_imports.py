from cen import CENetwork, filterModalities
from dfm import DFMNetwork
from lim import LIMNetwork
from sal import SALNetwork
from sen import SENNetwork
from ven import VENNetwork
from vis import VISNetwork

def network_builder(network_choice: str):
    network_modules = {
        "CEN": CENetwork,
        "DFM": DFMNetwork,
        "LIM": LIMNetwork,
        "SAL": SALNetwork,
        "SEN": SENNetwork,
        "VEN": VENNetwork,
        "VIS": VISNetwork
    }
    
    if network_choice not in network_modules:
        raise ValueError(f"Network module '{network_choice}' does not exist.")
        
    return network_modules[network_choice]

