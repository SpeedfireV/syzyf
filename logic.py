from burst_error_generator import burst_error_generator, random_message
from check_table_parity import check_table_parity
from line_slider_8x8 import slide_lines, get_columns, get_table_info
from burst_error_generator import burst_error_generator as beg

def encoder(data):
    slided_message = slide_lines(get_columns(data[::1]))
    print(data)
    print(slide_lines(get_columns(data[::1])))
    print(get_table_info(slided_message))
    additional_bits = check_table_parity(slided_message, True)
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
    decoded_parities = check_table_parity(slided_message, True)
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

    total_row_lines = 0
    for row_pos, row in enumerate(left_parity_errors):
        amount_of_errors = 0
        if row == 1:
            total_row_lines += 1
            amount_of_errors += 1
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
            total_row_lines += 1
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



    acceptable_error_poses = []
    potentially_wrong_bits = sorted(potentially_wrong_bits)

    print(f"Potentially wrong {potentially_wrong_bits}")
    for error_pos, potential_error in enumerate(potentially_wrong_bits):
        try:
            if potentially_wrong_bits[error_pos + total_number_of_errors - 1] - potential_error < 8:
                for i in range(total_number_of_errors):
                    if acceptable_error_poses.count(potentially_wrong_bits[error_pos + i]) == 0:
                        acceptable_error_poses.append(potentially_wrong_bits[error_pos + i])

        except IndexError:
            break
    if len(acceptable_error_poses) == total_number_of_errors:
        return acceptable_error_poses
    potential_error_packages = []
    for i in range(len(acceptable_error_poses) - total_number_of_errors + 1):
        if acceptable_error_poses[i + total_number_of_errors - 1] - acceptable_error_poses[i] < 8:
            potential_error_packages.append(acceptable_error_poses[i:i + total_number_of_errors])

    filtered_potential_error_packages = []
    for i in range(len(potential_error_packages)):
        basic_table = information_bits
        # print("Here")
        # print(basic_table)
        # print([i for i in range(64)])
        for errors in potential_error_packages:
            for error in errors:
                if basic_table[error] == 1:
                    basic_table[error] = 0
                else:
                    basic_table[error] = 1
            #
            # print(basic_table)
            # print(f"For {errors}")

            fixed_table_info = check_table_parity(slide_lines(get_columns(basic_table)), False)


            fixed_left_parities = fixed_table_info[0]
            fixed_right_parities = fixed_table_info[1]
            fixed_top_parities = fixed_table_info[2]
            fixed_bottom_parities = fixed_table_info[3]
            if fixed_left_parities == received_left_parities and fixed_right_parities == received_right_parities and fixed_top_parities == received_top_parities and fixed_bottom_parities == received_bottom_parities:
                filtered_potential_error_packages.append(errors)

    print(total_number_of_errors)
    print(total_row_lines)
    return sorted(acceptable_error_poses), sorted(potentially_wrong_bits),len(potential_error_packages), filtered_potential_error_packages, f"Lacking row lines? {not total_row_lines == total_number_of_errors}"



message = random_message()
print(message)
encoded_message = encoder(message)
transmitted_info = transmission(encoded_message)
print(decoder(transmitted_info))










