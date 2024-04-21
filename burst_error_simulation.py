import random
from random import randint

def random_message():
    message = [random.randint(0,1)for i in range(64)]
    return message
def burst_error_simulation(message):

    burst_start = randint(0,63)
    if 64 - burst_start < 8:
        burst_length = randint(0, 64 - burst_start)
    else:
        burst_length = randint(1, 7)
    print(message)
    falsified_bits = []
    for pos, letter in enumerate(message[burst_start:burst_start + burst_length + 1], burst_start):

        if randint(0,1) == 1 or burst_start + burst_length == pos or burst_start == pos:
            print(f"Changed {pos}. bit")
            falsified_bits.append(pos)
            if letter == "0":
                message[pos] = "1"
            else:
                message[pos] = "0"

    return message, falsified_bits, len(falsified_bits)



message = random_message()
falsified_message = burst_error_simulation(message)[0]
