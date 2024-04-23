def deshuffler(file_path_input, file_path_output):
    # Wczytanie danych z pliku wejściowego
    lines = []
    with open(file_path_input, 'r') as file:
        for line in file:
            line = line.strip()  # Usunięcie białych znaków z końca i początku linii
            lines.append(line)

    # Sprawdzenie, czy długość linii jest poprawna
    line_length = len(lines[0])
    for line in lines:
        if len(line) != line_length:
            raise ValueError("All lines in the input file must have the same length.")

    # Stworzenie listy wynikowej
    unmerged_lines = [''] * line_length

    # Rozdzielenie znaków na poszczególne linie
    for i in range(line_length):
        for j in range(len(lines)):
            unmerged_lines[i] += lines[j][i]

    # Zapisanie rozdzielonych linii do pliku wyjściowego
    with open(file_path_output, 'w') as file:
        for line in unmerged_lines:
            file.write(line + '\n')

# Przykład użycia
deshuffler("output.txt", "input_restored.txt")
