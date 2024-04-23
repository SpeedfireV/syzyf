def shuffler(file_path_input, file_path_output):
    # Wczytanie danych z pliku wejściowego
    lines = []
    with open(file_path_input, 'r') as file:
        for line in file:
            line = line.strip()  # Usunięcie białych znaków z końca i początku linii
            lines.append(line)

    # Sprawdzenie, czy liczba linii i ich długość są poprawne
    num_lines = len(lines)
    line_length = len(lines[0])
    for line in lines:
        if len(line) != line_length:
            raise ValueError("All lines in the input file must have the same length.")

    # Stworzenie listy wynikowej
    merged_lines = [''] * line_length

    # Połączenie znaków z poszczególnych linii
    for i in range(num_lines):
        for j in range(line_length):
            merged_lines[j] += lines[i][j]

    # Zapisanie połączonych linii do pliku wyjściowego
    with open(file_path_output, 'w') as file:
        for line in merged_lines:
            file.write(line + '\n')

# Przykład użycia
shuffler("encodedhamming.txt", "shuffledhamming.txt")
