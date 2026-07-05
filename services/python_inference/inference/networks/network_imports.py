# network_imports.py
def network_builder(network_choice: str):

    if network_choice == "CEN":
        from .cen import CENNetwork
        return CENNetwork
    elif network_choice == "LIM":
        from .lim import LIMNetwork
        return LIMNetwork

    network_modules = [
        "CEN",
        "LIM"
    ]
    
    if network_choice not in network_modules:
        raise ValueError(f"Network module '{network_choice}' does not exist.")
        
    return network_modules[network_choice]