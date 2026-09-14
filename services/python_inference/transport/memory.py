import json, random, asyncio
from watchfiles import watch, Change
from ..transport import middleware

memory_holder = []
neurons = None

int_to_string_map_single = {
    1: "one", 
    2: "two", 
    3: "three", 
    4: "four", 
    5: "five", 
    6: "six", 
    7: "seven", 
    8: "eight", 
    9: "nine",
    "1": 1, 
    "2": 2, 
    "3": 3, 
    "4": 4, 
    "5": 5, 
    "6": 6, 
    "7": 7, 
    "8": 8, 
    "9": 9,
}

int_to_string_map_single_edge = {
    11: "eleven", 
    12: "twelve", 
    13: "thirteen",
    "11": 11, 
    "12": 12, 
    "13": 13,
}

int_to_string_map_double = {
    10: "ten", 
    20: "twenty", 
    30: "thirty", 
    40: "forty", 
    50: "fifty", 
    60: "sixty", 
    70: "seventy", 
    80: "eighty", 
    90: "ninety", 
    100: "one hundred",
    "10": 10, 
    "20": 20, 
    "30": 30, 
    "40": 40, 
    "50": 50, 
    "60": 60, 
    "70": 70, 
    "80": 80, 
    "90": 90, 
    "100": 100
}

int_to_string_map_scale = {
    1: "ones", 
    2: "tens", 
    3: "hundred", 
    4: "thousand", 
    5: "ten thousands", 
    6: "hundred thousand", 
    7: "million", 
    8: "ten million", 
    9: "hundred million", 
    10: "billion",
}

async def continue_memory_transport(memory: dict[str, any]) -> bool:

    middleware.MEMORY = memory

    return True
    
async def memory_filter(change: Change, path: str) -> bool:

    if (change.modified):
        print("Neuron modified.")

    if (change.modified.bit_length > 5):
        print("Neuron potentially freed up or used.")

    return True

if (len(memory_holder) == 100):

    print(f"Loaded {len(neurons['neuron_status'])} neurons. Starting allocation...\n")
    
    try:
        with open('synaptic_neurons.json', 'r', encoding='utf-8') as file:
            
            neurons = json.load(file)
            print("Neurons activated:", neurons)

    except FileNotFoundError:
        print("Error: The file 'synaptic_neurons.json' could not be found.")
        print("Short term memory is not available, resorting to immediate memory storage")
        # Might need a dynamic short term memory creation on the fly
        # Else if graph database would need logic to sort the short term memory store vs
        # this type of memory store which is an immediate
        raise FileNotFoundError

    except json.JSONDecodeError:
        print("Error: The file contains invalid JSON syntax.")
        print("Short term memory glitched, refreshing..")
        # Need a dynamic JSON recreation logic
        raise json.JSONDecodeError


    for memory in memory_holder:

        memory_operation_iterate = 0 
        parse_memory = json.loads(memory) 
        
        neuron_status = neurons["neuron_status"]

        neuron_activated = False
        neuron_id = None

        while (neuron_activated != True):

            random_available_neuron = random.randint(1, 5000)

            memory_operation_iterate += 1

            if memory_operation_iterate == 20:
                
                print(f"Failsafe triggered for memory item {memory_holder.index(memory)}.")
                memory_operation_iterate = 0
                break

            if (neuron_status[random_available_neuron] == "Active"):

                random_available_neuron = random.randint(1, 5001)
                continue

            else:

                if (len(str(random_available_neuron)) in int_to_string_map_scale.keys()):

                    int_length = len(str(random_available_neuron))

                    if (int_length == 3):

                        int_string = str(random_available_neuron)
                        str_nums = []

                        for str_digit in int_string:

                            str_nums.append(int_to_string_map_single[str_digit])

                            if len(str_nums) == 1:
                                str_nums.append(int_to_string_map_scale[3])

                        str_nums[2] = int_to_string_map_double[int(str_nums[2])] + "0"

                        neuron_id = int("".join(str_nums))

                    if (int_length == 4):

                        int_string = str(random_available_neuron)
                        str_nums = []

                        for number in int_string:

                            str_nums.append(int_to_string_map_single[int(number)])

                            if len(str_nums) == 1:
                                str_nums.append(int_to_string_map_scale[4])

                            if len(str_nums) == 3:
                                str_nums.append(int_to_string_map_scale[3])

                            if len(str_nums) == 4:
                                str_nums.append(int_to_string_map_double[int(str_nums[2])] + "0")

                        neuron_id = int("".join(str_nums))

                    if (int_length > 4):
                        print("Brain cannot keep up with the neurons at the moment, allocating to a temporary cortex..")
                        break

                    int_string = str(random_available_neuron)
                    str_nums = []

                    for number in int_string:

                        if int(number) != 0:

                            get_double_digit = int_to_string_map_double[int(str_nums[0])] + "0"

                            str_nums.clear()

                            neuron_id = int("".join(str_nums))
                            
                        else: 
                            continue

                    double_digit = int_to_string_map_double[int(str_nums[1])] + "0"

                    str_nums[0] = double_digit

                    neuron_id = int("".join(str_nums))

                else:
                    # Randomize again if the chosen int is beyond the range, which is impossible but just in case
                    continue

                neurons["neuron_status"][random_available_neuron] = "Active"
                neurons["neuron_status"][neuron_int_to_string] = parse_memory # Assuming thisalso has the same format in json so they just be overwritten smoothly

                neuron_activated = True
                print(f"[{memory_holder.index(memory)+1}/100] Memory allocated to Neuron {random_available_neuron} (Attempts: {memory_operation_iterate})")

        asyncio.create_task(continue_memory_transport(memory))
        memory_operation_iterate = 0

synapse_watcher = watch("synaptic_neurons.json", watch_filter=memory_filter)