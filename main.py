from burst_error_generator import random_message, burst_error_generator
from check_table_parity import display_parities
from line_slider_8x8 import get_columns, slide_lines, get_data, get_table_parities
from table_display_8x8 import display_table, display_columns

if __name__ == '__main__':
    message = random_message()
    print("--- Original message ---")
    display_table(message)
    print("--- Creating Falsified Message ---")
    falsified_message = burst_error_generator(message)[0]
    print("--- Falsified message ---")
    display_table(falsified_message)

    slided_message = slide_lines(get_columns(message))
    print("CHECK PARITIES")
    additional_bits = get_table_parities(get_data(slided_message))
    message_to_send = get_data(slided_message)
    message_to_send.extend(additional_bits)
    print(message_to_send)
    print("--- Original Parites ---")
    display_parities(slide_lines(get_columns(message)))
    print("--- Falsified Parites ---")
    display_parities(slide_lines(get_columns(falsified_message)))