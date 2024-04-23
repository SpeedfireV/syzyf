def odczyt_danych(file_path_input, file_path_output):
    merged_text = ''
    with open(file_path_input, 'r') as file:
        for line in file:
            line = line.strip()  # Usunięcie białych znaków z końca i początku linii
            merged_text += ''.join([line[i] for i in range(len(line)) if i not in [0, 1, 2, 4, 8, 13, 14, 15]])

    # Zapisanie scalonego tekstu do pliku wyjściowego
    with open(file_path_output, 'w') as file:
        file.write(merged_text)

# Przykład użycia
odczyt_danych("encodedhamming.txt", "decodedhamming.txt")
