def create_table(data, numberOfRows):
    rows = []
    for i in range(numberOfRows):
        rows.append(data[i * 8:(i + 1) * 8])
    return rows

def display_table(data, numberOfRows):
    for i in range(numberOfRows):
        print(data[i * 8:(i + 1) * 8])

def display_columns(columns, numberOfRows):

    for i in range(numberOfRows):
        row = []
        for column in columns:
            row.append(column[i])
        print(row)