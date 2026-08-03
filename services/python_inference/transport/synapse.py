import json, os, random, asyncio
import numpy as np
import numba

@numba.jit(python=False)
class HilbertSpace:

    hilbert_space = np.array(dtype=np.complex128)

    def __init__(self, normal_cache: dict):

        '''
            Instantiates the HilbertSpace class along with the follow: hilbert_cache, hilbert_space_vector_id,
            hilbert_space_vector. The vector ID is a randomized 8-digit integer that serves as the key for 
            vector mapping.
        '''

        self.hilbert_cache = normal_cache
        self.hilbert_space_vector = np.array()
        self.processed_data = {}

        for datetime, data in enumerate(self.hilbert_cache):

            self.hilbert_space_vector_id = random.randint(10000000, 99999999)
            self.processed_data[self.hilbert_space_vector_id] = {datetime: data}

            if (datetime[-2:] - 30 == 0):
                self.processed_data[self.hilbert_space_vector_id]["operation"] == 1

            elif (datetime[-2:] - 30 >= 1):
                self.processed_data[self.hilbert_space_vector_id]["operation"] == 2


    def perform_operation(self) -> int:

        '''
            Performs mathematical operations with numba.jit class decorator for optimized
            CPU process. 
        '''

        for vector, data in enumerate(self.processed_data):

            if (data["operation"] == 1):

                self.hilbert_space_vector = np.array([1+2j, 3-4j])

                if (list(self.processed_data).index(vector) + 1 < len(list(self.processed_data))):

                    self.processed_data[vector][data] = self.processed_data[vector][data] + self.processed_data[vector][data]

            elif (data["operator"] == 2):

                self.hilbert_space_vector = np.array([1+2j, 3-4j])

                if (list(self.processed_data).index(vector) + 1 < len(list(self.processed_data))):
                
                    self.processed_data[vector][data] = self.processed_data[vector][data] * self.processed_data[vector][data]



        self.hilbert_space_vector = np.array([1+2j, 3-4j])
        self.hilbert_space = np.append(self.hilbert_space_vector, self.hilbert_space_vector_id)

        return self.hilbert_space_vector_id

    def lookup_space(self) -> np.ndarray:

        '''
            Returns the hilbert space to the Synapse object.
        '''

        return self.hilbert_space

class Synapse:

    synapse_hilbert_cache = {}

    synapse_normal_token_cache = {}
    synapse_normal_embeddings_cache = {}
    synapse_normal_chat_cache = {}

    def __init__(self):
        pass

    def load_to_cache(self, interaction: object):

        '''
            Appends the recent data retrieved from the application to the in-memory cache, 
            this data includes both the user's and the agent's interaction including the metadata.
        '''

        user_text = interaction["user"]["message"]
        agent_text = interaction["agent"]["message"]

        interaction_datetime = interaction["datetime"]

        self.synapse_normal_chat_cache["user"][interaction_datetime] = user_text
        self.synapse_normal_chat_cache["agent"][interaction_datetime] = agent_text

    def transform_hilbert_cache(self):

        '''
            Offloads the hilbert space mathematical operations to the HilbertSpace class.
            The instantiated Synapse's hilbert cache gets updated with the resulting vector
            and its corresponding vector ID.
        '''

        space = HilbertSpace(self.synapse_hilbert_cache)
        self.synapse_hilbert_cache[f"{space.perform_operation()}"] = space.hilbert_space_vector

    def get_data(self, key):
        if key in self.cache:
            return self.cache[key] # Cache Hit
        pass

        # SOON
        #data = fetch_neo()
        #self.synapse_normal_embeddings_cache[key] = data