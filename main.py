from burst_error_generator import random_message, burst_error_generator
from check_table_parity import check_table_parity
from line_slider_8x8 import get_columns, slide_lines, get_data, get_table_info
from logic import encoder, transmission, decoder
from table_display_8x8 import display_table, display_columns

if __name__ == '__main__':
    # message = random_message()
    # print("--- Original message ---")
    # display_table(message)
    # print("--- Creating Falsified Message ---")
    # falsified_message = burst_error_generator(message)[0]
    # print("--- Falsified message ---")
    # display_table(falsified_message)
    #
    # slided_message = slide_lines(get_columns(message))
    # print("CHECK PARITIES")
    # additional_bits = get_table_info(get_data(slided_message))
    # message_to_send = get_data(slided_message)
    # message_to_send.extend(additional_bits)
    # print(message_to_send)
    # print("--- Original Parites ---")
    # check_table_parity(slide_lines(get_columns(message)))
    # print("--- Falsified Parites ---")
    # check_table_parity(slide_lines(get_columns(falsified_message)))
    with open('tests.txt') as tests:
        working_amount = 0
        amount_of_tests = 30000
        not_defined = 0
        more_than_one_answer = 0
        correction_percentage = 0
        amount_of_errors = 0
        # Custom Test
        test_data = "0000000000000000000000000000000000000000000000000000000000000000"
        # 10110101
        # 00000011
        # 01101011
        # 00110010
        # 11111110
        # 11000001
        # 01010011
        # 01000111
        test_errors = "24 25 26 27 28 29 30 31"
        test_data = [eval(i) for i in test_data]
        falsified_bits = [eval(i) for i in test_errors.split(" ")]
        message = test_data
        encoded_message = encoder(message, True)
        transmitted_info = transmission(encoded_message, False, falsified_bits)
        resultant_falsified_bits = decoder(transmitted_info, 16,True)
        # Tests
        #
        # length = 0
        # amount = 0
        # not_working = []
        # for i in range(amount_of_tests):
        #
        #     test = list(tests.readline().strip())
        #     test = [eval(i) for i in test]
        #     falsified_bits = tests.readline().strip().split(" ")
        #     falsified_bits = [eval(i) for i in falsified_bits]
        #     amount_of_errors += len(falsified_bits)
        #     message = test
        #     encoded_message = encoder(message, False)
        #     transmitted_info = transmission(encoded_message, False, falsified_bits)
        #     resultant_falsified_bits = decoder(transmitted_info, 16, False)
        #     if resultant_falsified_bits == falsified_bits:
        #         working_amount += 1
        #         correction_percentage += len(falsified_bits)
        #     elif len(resultant_falsified_bits) == 0:
        #         not_defined += 1
        #     else:
        #         print(falsified_bits)
        #         not_working.append(falsified_bits)
        #         amount += 1
        #         length += len(falsified_bits)
        #         fixed_errors = 0
        #         for proposed_error_position in resultant_falsified_bits:
        #             if falsified_bits.count(proposed_error_position) > 0:
        #                 fixed_errors += 1
        #         correction_percentage += fixed_errors
        #
        #
        # else:
        #     print(f"Working on {working_amount} out of {amount_of_tests} which is {working_amount * 100 / amount_of_tests}%"
        #           f"\nAdditionally {not_defined} of answers to the tests were not defined which is {not_defined * 100 / amount_of_tests}%"
        #           f"\nCorrection of every error bit is: {correction_percentage * 100 / amount_of_errors}%"
        #           f"\nNot working were: {length / amount} of this length")
        #     for i in not_working:
        #         print(i)
        #
        #
        #
