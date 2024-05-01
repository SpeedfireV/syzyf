from burst_error_generator import burst_error_generator, random_message
from check_table_parity import check_table_parity
from line_slider_8x8 import slide_lines, get_columns, get_table_info
from burst_error_generator import burst_error_generator as beg

def encoder(data, debugMode):
    if debugMode:
        print("#ENCODER#")
        print("ORIGINAL MESSAGE:")
        for i in range(8):
            print(data[i:i + 8])
    slided_message = slide_lines(get_columns(data[::1]), numberOfRows=16)
    # print(data)
    # print(slide_lines(get_columns(data[::1])))
    # print(get_table_info(slided_message))
    if debugMode:
        print("SLIDED MESSAGE WITH PARITY CHECKS!:")
        additional_bits = check_table_parity(slided_message, 16,debugMode )
    else:
        additional_bits = check_table_parity(slided_message, 16,debugMode)
    whole_message = [data]
    whole_message.extend(additional_bits)
    return whole_message
def transmission(sended_message, debugMode, selected_error_bits):
    if debugMode:
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
    falsified_information = beg(information_bits)[0]
    sended_message[0] = falsified_information
    return sended_message

def decoder(received_message, numberOfRows, debugMode):
    if debugMode:
        print("#DECODER#")
    information_bits = received_message[0]
    slided_message = slide_lines(get_columns(information_bits), numberOfRows)
    received_left_parities = received_message[1]
    received_right_parities = received_message[2]
    received_top_parities = received_message[3]
    received_bottom_parities = received_message[4]
    if debugMode:
        print("SLIDED RECIEVED MESSAGE WITH PARITY CHECK:")
        decoded_parities = check_table_parity(slided_message, numberOfRows,debugMode)
    else:
        decoded_parities = check_table_parity(slided_message, numberOfRows, debugMode)
    decoded_left_parities = decoded_parities[0]
    decoded_right_parities = decoded_parities[1]
    decoded_top_parities = decoded_parities[2]
    decoded_bottom_parities = decoded_parities[3]
    left_parity_errors = []
    right_parity_errors = []
    top_parity_errors = []
    bottom_parity_errors = []
    # Calcute Parities
    for i in range(numberOfRows):
        if received_left_parities[i] != decoded_left_parities[i]:
            left_parity_errors.append(1)
        else:
            left_parity_errors.append(0)
        if received_right_parities[i] != decoded_right_parities[i]:
            right_parity_errors.append(1)
        else:
            right_parity_errors.append(0)
        if i < 8:
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



    for row_pos, row_value in enumerate(left_parity_errors):
        amount_of_errors = 0
        if row_value == 1:
            total_row_lines += 1
            amount_of_errors += 1
            if row_pos < numberOfRows // 2:
                for col_pos, col_value in enumerate(top_parity_errors[:4]):
                    if col_value == 1:
                        slided_error_pos = row_pos * 8 + col_pos
                        jump = col_pos * 2 * 8
                        potential_error_pos = slided_error_pos - jump
                        if potential_error_pos < 0:
                            potential_error_pos = numberOfRows * 8 + potential_error_pos
                        potentially_wrong_bits.append(potential_error_pos)
            else:
                for col_pos, col_value in enumerate(bottom_parity_errors[:4]):
                    if col_value == 1:
                        slided_error_pos = row_pos * 8 + col_pos
                        jump = col_pos * 2 * 8
                        potential_error_pos = slided_error_pos - jump
                        if potential_error_pos < 0:
                            potential_error_pos = numberOfRows * 8 + potential_error_pos
                        potentially_wrong_bits.append(potential_error_pos)
    for row_pos, row_value in enumerate(right_parity_errors):
        if row_value == 1:
            total_row_lines += 1
            if row_pos < numberOfRows // 2:
                for col_pos, col_value in enumerate(top_parity_errors[4:], 4):
                    if col_value == 1:
                        slided_error_pos = row_pos * 8 + col_pos
                        jump = col_pos * 2 * 8
                        potential_error_pos = slided_error_pos - jump
                        if potential_error_pos < 0:
                            potential_error_pos = numberOfRows * 8 + potential_error_pos
                        potentially_wrong_bits.append(potential_error_pos)
            else:
                for col_pos, col_value in enumerate(bottom_parity_errors[4:], 4):
                    if col_value == 1:
                        slided_error_pos = row_pos * 8 + col_pos
                        jump = col_pos * 2 * 8
                        potential_error_pos = slided_error_pos - jump
                        if potential_error_pos < 0:
                            potential_error_pos = numberOfRows * 8 + potential_error_pos
                        potentially_wrong_bits.append(potential_error_pos)



    acceptable_error_poses = []
    potentially_wrong_bits = sorted(potentially_wrong_bits)
    print(potentially_wrong_bits)
    for pos, index in enumerate(potentially_wrong_bits):
        if index >= 64:
            potentially_wrong_bits = potentially_wrong_bits[:pos]
            break
    print(potentially_wrong_bits)
    # print(f"Potentially wrong {potentially_wrong_bits}")
    for error_pos, potential_error in enumerate(potentially_wrong_bits):
        try:
            if potentially_wrong_bits[error_pos + total_number_of_errors - 1] - potential_error < 8:
                for i in range(total_number_of_errors):
                    if acceptable_error_poses.count(potentially_wrong_bits[error_pos + i]) == 0:
                        acceptable_error_poses.append(potentially_wrong_bits[error_pos + i])

        except IndexError:
            break
    if len(acceptable_error_poses) == total_number_of_errors:
        if debugMode:
            print("ERRORS OCCURED ON BITS:")

            for error in acceptable_error_poses:
                print(error)
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

            fixed_table_info = check_table_parity(slide_lines(get_columns(basic_table), 16), 16, False)


            fixed_left_parities = fixed_table_info[0]
            fixed_right_parities = fixed_table_info[1]
            fixed_top_parities = fixed_table_info[2]
            fixed_bottom_parities = fixed_table_info[3]
            if fixed_left_parities == received_left_parities and fixed_right_parities == received_right_parities and fixed_top_parities == received_top_parities and fixed_bottom_parities == received_bottom_parities:
                if not filtered_potential_error_packages.count(errors) > 0:
                    filtered_potential_error_packages.append(errors)

    # print(total_number_of_errors)
    # print(total_row_lines)
    #return sorted(acceptable_error_poses), sorted(potentially_wrong_bits),len(potential_error_packages), filtered_potential_error_packages, f"Lacking row lines? {not total_row_lines == total_number_of_errors}"
    if debugMode:
        print("ERRORS OCCURED ON BITS:")
        if len(filtered_potential_error_packages) == 0:
            print("0 Filtered Potential Errors")

        else:
            for error in filtered_potential_error_packages[0]:
                print(error)
    if filtered_potential_error_packages != []:
        return filtered_potential_error_packages[0]
    else:
        return []

if __name__ == "__main__":
    message = random_message()
    # print(message)
    encoded_message = encoder(message, False)
    transmitted_info = transmission(encoded_message, False)
    decoder(transmitted_info, False)










