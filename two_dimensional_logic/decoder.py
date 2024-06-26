from table_parities import get_table_parities
from data_formatter import get_columns
from line_slider import slide_lines


def decoder(received_message, number_of_rows, debug_mode):
    if debug_mode:
        print("#DECODER#")
    information_bits = received_message[0]
    slided_message = slide_lines(get_columns(information_bits), number_of_rows)
    received_row_parities = received_message[1]
    received_top_column_parities = received_message[2]
    received_bottom_column_parities = received_message[3]
    if debug_mode:
        print("SLIDED RECIEVED MESSAGE WITH PARITY CHECK:")
        decoded_parities = get_table_parities(slided_message, number_of_rows, debug_mode)
    else:
        decoded_parities = get_table_parities(slided_message, number_of_rows, debug_mode)
    decoded_row_parities = decoded_parities[0]
    decoded_top_column_parities = decoded_parities[1]
    decoded_bottom_column_parities = decoded_parities[2]
    row_parity_errors = []
    top_column_parity_errors = []
    bottom_column_parity_errors = []
    # Calcute Parities
    for i in range(number_of_rows):
        if received_row_parities[i] != decoded_row_parities[i]:
            row_parity_errors.append(1)
        else:
            row_parity_errors.append(0)
    for i in range(8):
        if i < 8:
            if received_top_column_parities[i] != decoded_top_column_parities[i]:
                top_column_parity_errors.append(1)
            else:
                top_column_parity_errors.append(0)
            if received_bottom_column_parities[i] != decoded_bottom_column_parities[i]:
                bottom_column_parity_errors.append(1)
            else:
                bottom_column_parity_errors.append(0)
    potentially_wrong_bits = []

    total_number_of_errors = row_parity_errors.count(1)
    # For Top Column
    for col_pos, col_value in enumerate(top_column_parity_errors):
        if col_value == 1:
            overflow = False
            overflow_value = 16 - (col_pos * 2)
            if overflow_value < 8:
                overflow = True
            for row_pos, row_value in enumerate(row_parity_errors[col_pos * 2:8], col_pos * 2):
                if row_value == 1:
                    slided_error_pos = row_pos * 8 + col_pos
                    jump = col_pos * 2 * 8  # Going back number of lines
                    potential_error_pos = slided_error_pos - jump
                    if potential_error_pos < 0:
                        potential_error_pos = number_of_rows * 8 + potential_error_pos
                    potentially_wrong_bits.append(potential_error_pos)
            if overflow:
                for row_pos, row_value in enumerate(row_parity_errors[0: 8 - overflow_value]):
                    if row_value == 1:
                        slided_error_pos = row_pos * 8 + col_pos
                        jump = col_pos * 2 * 8  # Going back number of lines
                        potential_error_pos = slided_error_pos - jump
                        if potential_error_pos < 0:
                            potential_error_pos = number_of_rows * 8 + potential_error_pos
                        potentially_wrong_bits.append(potential_error_pos)
    # For Bottom Column
    for col_pos, col_value in enumerate(bottom_column_parity_errors):
        if col_value == 1:
            start_slide = col_pos * 2 - 8
            if start_slide > 0:
                start_pos = 8 + start_slide
            else:
                start_pos = 8

            for row_pos, row_value in enumerate(row_parity_errors[start_pos:8 + col_pos * 2], start_pos):
                if row_value == 1:
                    slided_error_pos = row_pos * 8 + col_pos
                    jump = col_pos * 2 * 8  # Going back number of lines
                    potential_error_pos = slided_error_pos - jump
                    if potential_error_pos < 0:
                        potential_error_pos = number_of_rows * 8 + potential_error_pos
                    potentially_wrong_bits.append(potential_error_pos)

    acceptable_error_poses = []
    potentially_wrong_bits = sorted(potentially_wrong_bits)
    print(potentially_wrong_bits)
    for pos, index in enumerate(potentially_wrong_bits):
        if index >= 64:
            potentially_wrong_bits = potentially_wrong_bits[:pos]
            break
    print(potentially_wrong_bits)
    for error_pos, potential_error in enumerate(potentially_wrong_bits):
        try:
            if potentially_wrong_bits[error_pos + total_number_of_errors - 1] - potential_error < 8:
                for i in range(total_number_of_errors):
                    if acceptable_error_poses.count(potentially_wrong_bits[error_pos + i]) == 0:
                        acceptable_error_poses.append(potentially_wrong_bits[error_pos + i])

        except IndexError:
            break
    if len(acceptable_error_poses) == total_number_of_errors:
        if debug_mode:
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
        for errors in potential_error_packages:
            for error in errors:
                if basic_table[error] == 1:
                    basic_table[error] = 0
                else:
                    basic_table[error] = 1

            fixed_table_info = get_table_parities(slide_lines(get_columns(basic_table), 16), 16, False)

            fixed_row_parities = fixed_table_info[0]
            fixed_top_column_parities = fixed_table_info[1]
            fixed_bottom_column_parities = fixed_table_info[2]

            if fixed_row_parities == received_row_parities and fixed_top_column_parities == received_top_column_parities and fixed_bottom_column_parities == received_bottom_column_parities:
                if not filtered_potential_error_packages.count(errors) > 0:
                    filtered_potential_error_packages.append(errors)

    if debug_mode:
        print("ERRORS OCCURED ON BITS:")
        if len(filtered_potential_error_packages) == 0:
            print("0 Filtered Potential Errors")

        else:
            for error in filtered_potential_error_packages[0]:
                print(error)
    if filtered_potential_error_packages:
        return filtered_potential_error_packages[0]
    else:
        return []