import json, os, random, asyncio
import numpy as np
import numba

@numba.jit(python=False)
class HilbertSpace:

    hilbert_space = np.array(dtype=np.complex128)

    def __init__(self, hilbert_cache: np.ndarray):

        self.hilbert_cache = hilbert_cache
        self.hilbert_space_vector_id = random.randint(10000000, 99999999)
        self.hilbert_space_vector = np.array()

        pass

    def perform_operation(self) -> int:

        self.hilbert_space_vector = np.array([1+2j, 3-4j])
        self.hilbert_space = np.append(self.hilbert_space_vector, self.hilbert_space_vector_id)

        return self.hilbert_space_vector_id

    def lookup_space(self) -> np.ndarray:
        return self.hilbert_space

class Synapse:

    synapse_hilbert_cache = {}

    synapse_normal_token_cache = {}
    synapse_normal_embeddings_cache = {}
    synapse_normal_chat_cache = {}

    def __init__(self):
        pass

    def load_to_cache(self, interaction: object):

        user_text = interaction["user"]["message"]
        agent_text = interaction["agent"]["message"]

        interaction_datetime = interaction["datetime"]

        self.synapse_normal_chat_cache["user"][interaction_datetime] = user_text
        self.synapse_normal_chat_cache["agent"][interaction_datetime] = agent_text

    def transform_hilbert_cache(self):

        space = HilbertSpace(self.synapse_hilbert_cache)
        self.synapse_hilbert_cache[f"{space.perform_operation()}"] = space.hilbert_space_vector

    def get_data(self, key):
        if key in self.cache:
            return self.cache[key] # Cache Hit
        pass

        # SOON
        #data = fetch_neo()
        #self.synapse_normal_embeddings_cache[key] = data