from dataclasses import dataclass, field
import numpy as np
import datetime
from typing import TypedDict

@dataclass
class InteractionOutput(TypedDict):
    date: datetime.date
    sensory: dict[str, dict[str, str | bytearray | np.bytes_]] # {Sensory: {'Modality': {'Time': "", 'Data': }}}
    modalities: list[str] # ['Text', 'Audio', 'Image', 'Video']
    request_activation: list[str] # ['CEN', 'DFM', 'LIM', 'SAL', 'SEN', 'VEN', 'VIS']
 
@dataclass
class NormalCacheEntry(TypedDict):
    datetime: datetime.date # '2026-06-25T12:30:00.000Z' # From InteractionOutput.sensory.datetime
    data: InteractionOutput # Slice date first to avoid redundancy: del InteractionOutput["date"]

@dataclass
class NormalCacheStore(TypedDict):
    store: list[NormalCacheEntry]

@dataclass
class QuantumCacheEntry(TypedDict):
    pass

class QuantumCacheStore(TypedDict):
    pass