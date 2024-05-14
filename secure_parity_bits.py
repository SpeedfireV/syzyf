
def prepare_bits_to_secure(row_parities, top_column_parity):
    prepared_bits = [[],[],[]]
    parity_bits = row_parities + top_column_parity
    l = 0
    for k in [1,3]:
        if len(prepared_bits[k]) <= 11:
            for i in range(8):
                prepared_bits.append(parity_bits[l])
                l += 1
    return prepared_bits

def create_secure_table(prepared_bits):
    for t in prepared_bits:
        sec_table = []
        for _ in range(4):
            sec_table.append(['0'] * 4)

        positions_to_skip = [(0, 0), (0, 1), (0, 2), (1, 0), (2, 0)]
        bit_index = 0
        for i in range(4):
            for j in range(4):
                if (i, j) not in positions_to_skip:
                    sec_table[i][j] = prepared_bits[bit_index]
                    bit_index += 1

        return sec_table

def securing_table(sec_table):

    K1counter = [0] * 2  # Inicjalizacja listy na sumy jedynek w poszczególnych kolumnach

    # Iteracja po kolumnach 2, 4
    for K1column_index in [1, 3]:
        # Sumowanie jedynek w danej kolumnie
        for row_index in range(4):
            K1counter[K1column_index // 2] += int(sec_table[row_index][K1column_index])

    sec_table[0][1] = str(sum(K1counter) % 2)
    #########################################################################################
    K2counter = [0] * 2  # Inicjalizacja listy na sumy jedynek w poszczególnych kolumnach

    # Iteracja po kolumnach 3, 4
    for K2column_index in [2, 3]:
        # Sumowanie jedynek w danej kolumnie
        for row_index in range(4):
            K2counter[K2column_index // 2] += int(sec_table[row_index][K2column_index])

    sec_table[0][2] = str(sum(K2counter) % 2)
    #########################################################################################

    R1counter = [0] * 2  # Inicjalizacja listy na sumy jedynek w poszczególnych wierszach

    # Iteracja po kolumnach 2, 4
    for R1row_index in [1, 3]:
        # Sumowanie jedynek w danej kolumnie
        for column_index in range(4):
            R1counter[R1row_index // 2] += int(sec_table[R1row_index][column_index])

    sec_table[1][0] = str(sum(R1counter) % 2)
    #########################################################################################

    R2counter = [0] * 4  # Inicjalizacja listy na sumy jedynek w poszczególnych wierszach

    # Iteracja po kolumnach 3, 4
    for R2row_index in [2, 3]:
        # Sumowanie jedynek w danej kolumnie
        for column_index in range(4):
            R2counter[R2row_index // 2] += int(sec_table[R2row_index][column_index])

    sec_table[2][0] = str(sum(R2counter) % 2)
    #########################################################################################

    Allcounter = 0

    for x in range(4):
        for y in range(4):
            if int(sec_table[x][y]) == 1:
                Allcounter += 1

    sec_table[0][0] = str(Allcounter % 2)

    return sec_table