def split_and_pad_bits(file_path_input, file_path_output):
    with open(file_path_input, 'r') as file:
        data = file.read().strip()

    if len(data) != 64:
        raise ValueError("Input file does not contain 64 bits.")

    # Dziel na 8-bitowe grupy i dodaj zera
    bits_padded = [data[i:i+8] + '000' for i in range(0, len(data), 8)]

    # Zapisz do pliku
    with open(file_path_output, 'w') as file:
        for bits in bits_padded:
            file.write(bits + '\n')

# Użycie funkcji
split_and_pad_bits("input.txt", "hamminginput.txt")
