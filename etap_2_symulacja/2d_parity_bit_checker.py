import itertools
from itertools import product

import sympy
from sympy import divisors

from etap_2_symulacja.charts.bar_chart import make_bar_chart


def get_dividers(number):
    custom_dividors = divisors(number)
    custom_dividors.pop(0)  # delete 1
    new_dividors = []
    for divider in custom_dividors:
        if divider < number // 2 \
                and not number // divider in new_dividors:
            new_dividors.append(divider)
    return new_dividors



def false_parity_check_results(number_of_bits, burst_size):
    sample_bits = [0 for i in range(number_of_bits)]
    combinations = []
    for i in product([0, 1], repeat=burst_size):
        if i.count(1) != 1:
            combinations.append(i)
    combinations = combinations[1:]
    all_combinations = []
    for combination in combinations:
        for i in range(0, number_of_bits - burst_size + 1):
            new_combination = sample_bits[:i]
            new_combination.extend(list(combination))
            new_combination.extend(sample_bits[i + burst_size:])
            all_combinations.append(new_combination)
    final_combinations = []
    for pos, combination in enumerate(all_combinations):
        if not combination in all_combinations[pos + 1:]:
            final_combinations.append(combination)
    new_dividers = get_dividers(number_of_bits)
    size_info = []
    for divider in new_dividers:
        # with 64 zero bytes every column and row has to be equal to 1
        total_number_of_fake_combinations = 0
        print(f"Total number of fake combinations for {divider}x{number_of_bits//divider}:")
        size_data = [f"{divider}x{number_of_bits//divider}"]
        for combination in final_combinations:
            row_values = []
            column_values = []
            batched_combination = itertools.batched(combination, divider)
            row_wrong = False
            for row in batched_combination:
                if row.count(1) % 2 == 0:
                    row_values.append(0)
                else:
                    row_wrong = True
                    break
                    # row_values.append(1)
            if row_wrong:
                continue
            for i in range(divider):
                column = combination[i::divider]
                if column.count(1) % 2 == 0:
                    column_values.append(0)
                else:
                    row_wrong = True
                    break
                    # column_values.append(1)
            if not row_wrong:
                total_number_of_fake_combinations += 1
        size_data.append(total_number_of_fake_combinations)
        size_info.append(size_data)
        print(total_number_of_fake_combinations)






    print(f"Liczba wszystkich fałszywie pozytywnych kombinacji dla burst-errora długości max. {burst_size}  - {len(final_combinations)}")
    return size_info

if __name__ == "__main__":
    max_bit_error = []
    eight_bit_error = []
    for i in range(9, 19):
        if not sympy.isprime(i):
            if i < 21:

                print("next", str(i))
                eight_bit_error.append(false_parity_check_results(i, 8))
                print("next", str(i))
                max_bit_error.append(false_parity_check_results(i, i))
            else:
                print("next", str(i))
                eight_bit_error.append(false_parity_check_results(i, 8))
    print(max_bit_error)
    print(eight_bit_error)
    x_axis = []
    for package in eight_bit_error:
        for values in package:
            x_axis.append(values[0])
    print(x_axis)
    y1 = []
    for package in eight_bit_error:
        for values in package:
            y1.append(values[1])

    y2 = []
    for package in max_bit_error:
        for values in package:
            y2.append(values[1])
    print(y1, y2)
    make_bar_chart(x_axis, y1, y2)
