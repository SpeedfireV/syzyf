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
        left_parity = row[:4].count(1) % 2
        right_parity = row[4:].count(1) % 2
        print(f"{left_parity} | {row} | {right_parity}")
        for pos, bit in enumerate(row):
            columns[pos].append(bit)

    top_column_parities = []
    bottom_column_parities = []
    for column in columns:
        top_column_parities.append(column[:4].count(1) % 2)
        bottom_column_parities.append(column[4:].count(1) % 2)
    print("     --- Top Parity ---")
    print(f"    {top_column_parities}")
    print("     --- Bottom Parity ---")
    print(f"    {bottom_column_parities}")