from burst_error_generator import random_message, burst_error_generator
from check_table_parity import display_parities
from line_slider_8x8 import get_columns, slide_lines
from table_display_8x8 import display_table, display_columns

if __name__ == '__main__':
    message = random_message()
    print("--- Original message ---")
    display_table(message)
    falsified_message = burst_error_generator(message)[0]
    print(message == falsified_message)
    print(message)
    print(falsified_message)
    slided_message = slide_lines(get_columns(message))
    print("--- Falsified message ---")
    display_table(falsified_message)
    print("--- Slided Original message ---")
    display_columns(slide_lines(get_columns(message)))
    print("--- Slided Falsified message ---")
    display_columns(slide_lines(get_columns(falsified_message)))
    print("--- Original Parites ---")
    display_parities(slide_lines(get_columns(message)))
    print("--- Falsified Parites ---")
    display_parities(slide_lines(get_columns(falsified_message)))