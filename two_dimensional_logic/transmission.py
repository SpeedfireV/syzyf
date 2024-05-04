from burst_error_generator import burst_error_generator


def transmission(sended_message, debug_mode, selected_error_bits):
    if debug_mode:
        print("#TRANSMISSION#")
    information_bits = sended_message[0][::1]
    if selected_error_bits is not None:
        for bit in selected_error_bits:
            if information_bits[bit] == 1:
                information_bits[bit] = 0
            else:
                information_bits[bit] = 1
        sended_message[0] = information_bits
        return sended_message
    falsified_information = burst_error_generator(information_bits)[0]
    sended_message[0] = falsified_information
    return sended_message