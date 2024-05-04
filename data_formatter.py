def get_columns(data):
    columns = []

    for pos, bit in enumerate(data):
        if len(columns) < pos % 8 + 1:
            columns.append([bit])
        else:
            columns[pos % 8].append(bit)

    return columns

def create_table(data, number_of_rows):
    rows = []
    for i in range(number_of_rows):
        rows.append(data[i * 8:(i + 1) * 8])
    return rows