from cen import CENetwork, filterModalities
from dfm import DFMNetwork
from lim import LIMNetwork
from sal import SALNetwork
from sen import SENNetwork
from ven import VENNetwork
from vis import VISNetwork

def networkBuilder(networkChoice):
    networkModules = {
        "CEN": CENetwork,
        "DFM": DFMNetwork,
        "LIM": LIMNetwork,
        "SAL": SALNetwork,
        "SEN": SENNetwork,
        "VEN": VENNetwork,
        "VIS": VISNetwork
    }
    
    if networkChoice not in networkModules:
        raise ValueError(f"Network module '{networkChoice}' does not exist.")
        
    return networkModules[networkChoice]

