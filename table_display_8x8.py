def create_table(data, number_of_rows):
    rows = []
    for i in range(number_of_rows):
        rows.append(data[i * 8:(i + 1) * 8])
    return rows
