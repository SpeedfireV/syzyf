from table_display_8x8 import create_table


def display_parities(data):
    print(f"GOT {data}")
    new_data = []
    for row in data:
        for bit in row:
            new_data.append(bit)
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
