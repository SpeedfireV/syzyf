from table_display_8x8 import create_table


def display_parities(data):
    new_data = []
    for i in range(8):
        for column in data:
            new_data.append(column[i])
    data = new_data
    rows: list[list[int]] = create_table(data)
    columns = [[] for i in range(8)]
    for row in rows:
        parity = row.count(1) % 2
        print(f"{row} | {parity}")
        for pos, bit in enumerate(row):
            columns[pos].append(bit)
    column_parities = []
    for column in columns:
        column_parities.append(column.count(1) % 2)
    print("--- Parity ---")
    print(column_parities)