import itertools
import math
from itertools import product
import sympy
import matplotlib.pyplot as plt
import numpy as np

bit_length_dict = {}

length = 9

for k in range(length, length + 1):
    if not sympy.isprime(k):
        for i in product([0,1], repeat=length):
            if bit_length_dict.get(k) != None:
                current_list = bit_length_dict[k]
                current_list.append(i)
                bit_length_dict[k] = current_list
            else:
                bit_length_dict[k] = [i]

class ParityChecking:
    def __init__(self, vertical_values, horizontal_values):
        self.vertical_values = vertical_values
        self.horizontal_values = horizontal_values
    def __str__(self):
        return str(self.vertical_values) + " " + str(self.horizontal_values)


overlapping_values = {}

for key, v in bit_length_dict.items():
    prime_factors = sympy.primefactors(key)
    for value in v:
        for factor in prime_factors:
            horizontal_values = []
            vertical_values = []
            for batch in itertools.batched(value, factor):
                if batch.count(1) % 2 == 0:
                    is_pair = 1
                else:
                    is_pair = 0
                vertical_values.append(is_pair)
            vertical_lines = []
            for i in range(factor):

                line = []

                for j in range(len(value) // factor):
                    line.append(value[j * factor + i])
                vertical_lines.append(line)
            for vertical_line in vertical_lines:
                if vertical_line.count(1) % 2 == 0:
                    is_pair = 1
                else:
                    is_pair = 0
                horizontal_values.append(is_pair)
            parity_check = ParityChecking(vertical_values, horizontal_values)
            if overlapping_values.get(len(value)) != None:
                if overlapping_values.get(len(value)).get(parity_check) != None:
                    overlapping_values[len(value)][parity_check].append(value)
                else:
                    current_dict = overlapping_values[len(value)]
                    current_dict[parity_check] = [value]
                    overlapping_values[len(value)] =current_dict
            else:
                overlapping_values[len(value)] = {parity_check: [value]}
plot_info_x = []
plot_info_y = []
overall_y_size = []
for key,value in overlapping_values.items():
    fact_value = math.factorial(key)
    print(f"For length {key}:")
    number_of_occurences = -1
    happened = set()
    for k,v in value.items():
        number_of_occurences = -1

        for ke, va in value.items():
            if ke.vertical_values == k.vertical_values and ke.horizontal_values == k.horizontal_values:
                print(va[0][0:3], "\n", va[0][3:6], "\n", va[0][6:], "\nnext")
                number_of_occurences += 1


        if number_of_occurences in happened:
            break
        else:
            happened.add(number_of_occurences)
            print("Dimensions: " + str(len(k.vertical_values)) + "x" + str(len(k.horizontal_values)))
            print(number_of_occurences)
            plot_info_x.append(str(len(k.vertical_values)) + "x" + str(len(k.horizontal_values)))
            plot_info_y.append(number_of_occurences)
            overall_y_size.append(fact_value)
x = np.array(plot_info_x)
y = np.array(plot_info_y)
overall = np.array(overall_y_size)
print(y)
plt.xticks(range(len(plot_info_x)), plot_info_x, rotation=30)
bar1 = plt.bar(np.arange(len(y)), y, align='center', color='g')

plt.xlabel('Rozmiary dwuwymiarowej tablicy')
plt.ylabel('Liczba wyników fałszywie pozytywnych')
for rect in bar1:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2.0, height, f'{height:.0f}', ha='center', va='bottom')
plt.tight_layout()
plt.savefig("parity.png")
plt.show()








