def read_11_bits_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read().strip()
    if len(data) != 11:
        raise ValueError("Input file does not contain 11 bits.")
    return data

def create_hamming_table(bits):
    hamming_table = []
    for _ in range(4):
        hamming_table.append(['0'] * 4)

    # Umieszczenie bitów z pliku w odpowiednich miejscach
    positions_to_skip = [(0, 0), (0, 1), (0, 2), (1, 0), (2, 0)]
    bit_index = 0
    for i in range(4):
        for j in range(4):
            if (i, j) not in positions_to_skip:
                hamming_table[i][j] = bits[bit_index]
                bit_index += 1

    return hamming_table

def calculate_parity_bits(hamming_table):
    K1counter = [0] * 2  # Inicjalizacja listy na sumy jedynek w poszczególnych kolumnach

    # Iteracja po kolumnach 2, 4
    for K1column_index in [1, 3]:
        # Sumowanie jedynek w danej kolumnie
        for row_index in range(4):
            K1counter[K1column_index // 2] += int(hamming_table[row_index][K1column_index])

    hamming_table[0][1] = str(sum(K1counter) % 2)
#########################################################################################
    K2counter = [0] * 2  # Inicjalizacja listy na sumy jedynek w poszczególnych kolumnach

    # Iteracja po kolumnach 3, 4
    for K2column_index in [2, 3]:
        # Sumowanie jedynek w danej kolumnie
        for row_index in range(4):
            K2counter[K2column_index // 2] += int(hamming_table[row_index][K2column_index])

    hamming_table[0][2] = str(sum(K2counter) % 2)
#########################################################################################

    R1counter = [0] * 2  # Inicjalizacja listy na sumy jedynek w poszczególnych wierszach

    # Iteracja po kolumnach 2, 4
    for R1row_index in [1, 3]:
        # Sumowanie jedynek w danej kolumnie
        for column_index in range(4):
            R1counter[R1row_index // 2] += int(hamming_table[R1row_index][column_index])

    hamming_table[1][0] = str(sum(R1counter) % 2)

#########################################################################################

    R2counter = [0] * 4  # Inicjalizacja listy na sumy jedynek w poszczególnych wierszach

    # Iteracja po kolumnach 3, 4
    for R2row_index in [2, 3]:
        # Sumowanie jedynek w danej kolumnie
        for column_index in range(4):
            R2counter[R2row_index // 2] += int(hamming_table[R2row_index][column_index])

    hamming_table[2][0] = str(sum(R2counter) % 2)

#########################################################################################

    Allcounter = 0

    for x in range(4):
        for y in range(4):
            if int(hamming_table[x][y]) == 1:
                Allcounter += 1

    hamming_table[0][0] = str(Allcounter % 2)

##############################################################################################
def write_encoded_bits_to_file(hamming_tables, file_path):
    with open(file_path, 'w') as file:
        for table in hamming_tables:
            bit_count = 0
            for row in table:
                file.write(''.join(row))
                bit_count += len(row)
                if bit_count % 16 == 0:  # Dodaj znak nowej linii co 16 bitów
                    file.write('\n')

file_path_input = "hamminginput.txt"  # Zakładając, że dane są w pliku encoded_bits_input.txt
hamming_tables = []

with open(file_path_input, 'r') as file:
    for _ in range(8):
        bits_11 = file.readline().strip()  # Odczytaj jedną linię (11 bitów)
        hamming_table = create_hamming_table(bits_11)
        calculate_parity_bits(hamming_table)
        hamming_tables.append(hamming_table)

file_path_output = "encodedhamming.txt"  # Plik wyjściowy
write_encoded_bits_to_file(hamming_tables, file_path_output)
