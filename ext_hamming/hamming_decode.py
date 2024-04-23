
def read_lines_to_variables(file_path):
    variables = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            variable = line.strip().replace(" ", "")  # Usunięcie spacji i znaków końca linii
            variables.append(variable)
    return variables


def create_hamming_table(bits):
    hamming_table = []
    for _ in range(4):
        hamming_table.append(['0'] * 4)

    bit_index = 0
    for i in range(4):
        for j in range(4):
            hamming_table[i][j] = bits[bit_index]
            bit_index += 1

    return hamming_table

def check_parity_bits(hamming_table):

    bladlokalny = ''
    K1counter = [0] * 2  # Inicjalizacja listy na sumy jedynek w poszczególnych kolumnach

    # Iteracja po kolumnach 2, 4
    for K1column_index in [1, 3]:
        # Sumowanie jedynek w danej kolumnie
        for row_index in range(4):
            K1counter[K1column_index // 2] += int(hamming_table[row_index][K1column_index])

    bladlokalny += str(sum(K1counter) % 2)

    K2counter = [0] * 2  # Inicjalizacja listy na sumy jedynek w poszczególnych kolumnach

    # Iteracja po kolumnach 3, 4
    for K2column_index in [2, 3]:
        # Sumowanie jedynek w danej kolumnie
        for row_index in range(4):
            K2counter[K2column_index // 2] += int(hamming_table[row_index][K2column_index])

    bladlokalny += str(sum(K2counter) % 2)

    R1counter = [0] * 2  # Inicjalizacja listy na sumy jedynek w poszczególnych wierszach

    # Iteracja po kolumnach 2, 4
    for R1row_index in [1, 3]:
        # Sumowanie jedynek w danej kolumnie
        for column_index in range(4):
            R1counter[R1row_index // 2] += int(hamming_table[R1row_index][column_index])

    bladlokalny += str(sum(R1counter) % 2)

    R2counter = [0] * 4  # Inicjalizacja listy na sumy jedynek w poszczególnych wierszach

    # Iteracja po kolumnach 3, 4
    for R2row_index in [2, 3]:
        # Sumowanie jedynek w danej kolumnie
        for column_index in range(4):
            R2counter[R2row_index // 2] += int(hamming_table[R2row_index][column_index])

    bladlokalny += str(sum(R2counter) % 2)

    Allcounter = 0

    for x in range(4):
        for y in range(4):
            if int(hamming_table[x][y]) == 1:
                Allcounter += 1

    bladlokalny += str(Allcounter % 2)

    return bladlokalny

def wyliczeniepozycjibledu(wartoscbitowa):
    # Sprawdzenie, czy łańcuch zawiera 7 znaków
    if len(wartoscbitowa) != 5:
        raise ValueError("Input string must contain 5 characters.")

    # Konwersja łańcucha binarnego na liczbę dziesiętną
    pozycjabledu = int(wartoscbitowa, 2)
    if pozycjabledu != 0:
        print(f'Błąd na pozycji: {pozycjabledu}')
    else:
        print('Błąd nie występuje')

zmienne = read_lines_to_variables('encodedhamming.txt')
for bits in zmienne:
    hamming_table = create_hamming_table(bits)
    pozycjebledow = check_parity_bits(hamming_table)
    wyliczeniepozycjibledu(pozycjebledow)
