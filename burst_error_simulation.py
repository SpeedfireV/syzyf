import random


def random_message():
    message = [random.randint(0,1)for i in range(64)]
    return message
def burst_error_simulation(message, always_burst_eight):
    falsified_message = []
    falsified_message = message
    burst_length = 0
    for i in range(64):
        if burst_length == 0:
            if random.randint(0,63) == 63:
                print(f"Burst happened on {i+1} bit")
                current_sign = falsified_message[i]
                if current_sign == 1:
                    falsified_message[i] = 0
                else:
                    falsified_message[i] = 1
                burst_length = 1
        elif burst_length == 7 or (not always_burst_eight and random.randint(0,8) == 8):
            current_sign = falsified_message[i]
            if current_sign == 1:
                falsified_message[i] = 0
            else:
                falsified_message[i] = 1
            print(f"Burst ended on {i + 1} bit")
            return falsified_message
        else:
            burst_length += 1
            if random.randint(0,1) == 1:
                current_sign = falsified_message[i]
                print(f"Bit {i + 1} was swapped")
                if current_sign == 1:
                    falsified_message[i] = 0
                else:
                    falsified_message[i] = 1

    return falsified_message



message = random_message()
falsified_message = burst_error_simulation(message, False)
