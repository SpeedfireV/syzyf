import random
from random import randint

def random_message():
    message = [random.randint(0,1)for i in range(64)]
    return message
def burst_error_generator(message):

    burst_start = randint(0,62)
    if 64 - burst_start < 8:
        burst_length = randint(0, 64 - burst_start)
    else:
        burst_length = randint(2, 7)
    falsified_bits = []
    falsified_message = message[::1]
    for pos, letter in enumerate(message[burst_start:burst_start + burst_length + 1], burst_start):
        if randint(0,1) == 1 or burst_start + burst_length == pos or burst_start == pos:
            falsified_bits.append(pos)
            print(f"{pos} was falsified")
            if letter == 0:
                falsified_message[pos] = 1
            else:
                falsified_message[pos] = 0
    return falsified_message, falsified_bits, len(falsified_bits)

def write_tests_to_file(amount):
    informations = []
    changed_bits = []
    for i in range(amount):
        while True:
            message = random_message()
            if message in informations:
                continue
            error_message, falsified_bits, _ = burst_error_generator(message)
            informations.append(error_message)
            changed_bits.append(falsified_bits)
            break
    with open("tests.txt", "w") as file:
        for pos, message in enumerate(informations):
            file.write(''.join(str(e) for e in message) + "\n")
            file.write(' '.join(str(e) for e in changed_bits[pos])+ "\n")