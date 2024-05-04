from table_parities import get_table_parities
from data_formatter import get_columns
from line_slider import slide_lines


def encoder(data, debug_mode):
    if debug_mode:
        print("#ENCODER#")
        print("ORIGINAL MESSAGE:")
        for i in range(8):
            print(data[i:i + 8])
    slided_message = slide_lines(get_columns(data[::1]), number_of_rows=16)
    if debug_mode:
        print("SLIDED MESSAGE WITH PARITY CHECKS!:")
        additional_bits = get_table_parities(slided_message, 16, debug_mode)
    else:
        additional_bits = get_table_parities(slided_message, 16, debug_mode)
    whole_message = [data]
    whole_message.extend(additional_bits)
    return whole_message
