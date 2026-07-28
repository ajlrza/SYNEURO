import json, os, random, asyncio
from watchfiles import watch, Change

memory_holder = []
neurons = None

async def continue_memory_transport(memory_iter) -> bool:
    neuron_activated = False
    while (neuron_activated != True):
                if (neuron_status[random_available_neuron] == "Active"):
                    continue
                else:
                    neuron_int_to_string = None # add function here
                    neurons["neuron_status"]["random_available_neuron"] == "Active"
                    neurons["neuron_status"]["neuron_int_to_string"] == memory # Assuming thisalso has the same format in json so they just be overwritten smoothly
                    neuron_activated = True
    return True
    

async def memory_filter(change: Change, path: str) -> bool:

    if (change.modified):
        print("Neuron modified.")

    if (change.modified > 5):
        print("Neuron potentially freed up or used.")

    return True

if (len(memory_holder) == 100):

    try:
        with open('synaptic_neurons.json', 'r', encoding='utf-8') as file:
            neurons = json.load(file)
            print("Neurons activated:", neurons)
    except FileNotFoundError:
        print("Error: The file 'synaptic_neurons.json' could not be found.")
    except json.JSONDecodeError:
        print("Error: The file contains invalid JSON syntax.")

    memory_operation_iterate = 0

    for memory in memory_holder:
        parse_memory = json.parse(memory)
        neuron_status = neurons["neuron_status"]
        random_available_neuron = random.random(1, 5001)
        neuron_activated = False
        while (neuron_activated != True):
            memory_operation_iterate += 1
            if (neuron_status[random_available_neuron] == "Active"):
                continue
            else:
                neuron_int_to_string = None # add function here
                neurons["neuron_status"]["random_available_neuron"] == "Active"
                neurons["neuron_status"]["neuron_int_to_string"] == memory # Assuming thisalso has the same format in json so they just be overwritten smoothly

            if (memory_operation_iterate == 20):
                break

        asyncio.create_task(continue_memory_transport(memory))
        memory_operation_iterate = 0

synapse_watcher = watch("synaptic_neurons.json", watch_filter=memory_filter())




