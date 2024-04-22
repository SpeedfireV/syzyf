def create_table(data):
    rows = []
    for i in range(8):
        rows.append(data[i * 8:(i + 1) * 8])
    return rows

def display_table(data):
    for i in range(8):
        print(data[i * 8:(i + 1) * 8])

def display_columns(columns):

    for i in range(8):
        row = []
        for column in columns:
            row.append(column[i])
        print(row)