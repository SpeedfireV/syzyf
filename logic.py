from burst_error_generator import burst_error_generator, random_message
from check_table_parity import check_table_parity
from line_slider_8x8 import slide_lines, get_columns, get_table_info
from burst_error_generator import burst_error_generator as beg

def encoder(data):
    slided_message = slide_lines(get_columns(data[::1]))
    print(data)
    print(slide_lines(get_columns(data[::1])))
    print(get_table_info(slided_message))
    additional_bits = check_table_parity(slided_message)
    whole_message = [data]
    whole_message.extend(additional_bits)
    return whole_message
def transmission(sended_message):
    information_bits = sended_message[0]
    falsified_information = beg(information_bits)[0]
    sended_message[0] = falsified_information
    return sended_message

def decoder(received_message):
    information_bits = received_message[0]
    slided_message = slide_lines(get_columns(information_bits))
    received_left_parities = received_message[1]
    received_right_parities = received_message[2]
    received_top_parities = received_message[3]
    received_bottom_parities = received_message[4]
    decoded_parities = check_table_parity(slided_message)
    decoded_left_parities =  decoded_parities[0]
    decoded_right_parities = decoded_parities[1]
    decoded_top_parities = decoded_parities[2]
    decoded_bottom_parities = decoded_parities[3]
    left_parity_errors = []
    right_parity_errors = []
    top_parity_errors = []
    bottom_parity_errors = []
    for i in range(8):
        if received_left_parities[i] != decoded_left_parities[i]:
            left_parity_errors.append(1)
        else:
            left_parity_errors.append(0)
        if received_right_parities[i] != decoded_right_parities[i]:
            right_parity_errors.append(1)
        else:
            right_parity_errors.append(0)
        if received_top_parities[i] != decoded_top_parities[i]:
            top_parity_errors.append(1)
        else:
            top_parity_errors.append(0)
        if received_bottom_parities[i] != decoded_bottom_parities[i]:
            bottom_parity_errors.append(1)
        else:
            bottom_parity_errors.append(0)

    potentially_wrong_bits = []

    total_number_of_errors = bottom_parity_errors.count(1) + top_parity_errors.count(1)

    for row_pos, row in enumerate(left_parity_errors):
        if row == 1:
            if row_pos < 4:
                for col_pos, col in enumerate(top_parity_errors[:4]):
                    if col == 1:
                        slided_error_pos = row_pos * 8 + col_pos
                        jump = col_pos * 8
                        potential_error_pos = slided_error_pos - jump
                        if potential_error_pos < 0:
                            potential_error_pos = 64 + potential_error_pos
                        potentially_wrong_bits.append(potential_error_pos)
            else:
                for col_pos, col in enumerate(bottom_parity_errors[:4]):
                    if col == 1:
                        slided_error_pos = row_pos * 8 + col_pos
                        jump = col_pos * 8
                        potential_error_pos = slided_error_pos - jump
                        if potential_error_pos < 0:
                            potential_error_pos = 64 + potential_error_pos
                        potentially_wrong_bits.append(potential_error_pos)
    for row_pos, row in enumerate(right_parity_errors):
        if row == 1:
            if row_pos < 4:
                for col_pos, col in enumerate(top_parity_errors[4:], 4):
                    if col == 1:
                        slided_error_pos = row_pos * 8 + col_pos
                        jump = col_pos * 8
                        potential_error_pos = slided_error_pos - jump
                        if potential_error_pos < 0:
                            potential_error_pos = 64 + potential_error_pos
                        potentially_wrong_bits.append(potential_error_pos)
            else:
                for col_pos, col in enumerate(bottom_parity_errors[4:], 4):
                    if col == 1:
                        slided_error_pos = row_pos * 8 + col_pos
                        jump = col_pos * 8
                        potential_error_pos = slided_error_pos - jump
                        if potential_error_pos < 0:
                            potential_error_pos = 64 + potential_error_pos
                        potentially_wrong_bits.append(potential_error_pos)


    acceptable_error_pos = []

    for error_pos, potential_error in enumerate(potentially_wrong_bits):
        try:
            if potentially_wrong_bits[error_pos + total_number_of_errors - 1] - potential_error <= 8:
                for pos in potentially_wrong_bits[error_pos:error_pos + total_number_of_errors - 1 + 1]:
                    acceptable_error_pos.append(potentially_wrong_bits[error_pos])

        except IndexError:
            break
    return sorted(acceptable_error_pos),  sorted(potentially_wrong_bits)



message = random_message()
print(message)
encoded_message = encoder(message)
transmitted_info = transmission(encoded_message)
print(decoder(transmitted_info))










