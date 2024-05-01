from table_display_8x8 import create_table


def check_table_parity(data, numberOfRows,debugMode):
    new_data = []
    for i in range(numberOfRows):
        for column in data:
            new_data.append(column[i])
    data = new_data
    rows: list[list[int]] = create_table(data, numberOfRows)
    columns = [[] for i in range(8)]
    left_parities = []
    right_parities = []
    for row in rows:
        left_parity = row[:4].count(1) % 2
        right_parity = row[4:].count(1) % 2
        left_parities.append(left_parity)
        right_parities.append(right_parity)
        if debugMode:
            print(f"{left_parity} | {row} | {right_parity}")
        for pos, bit in enumerate(row):
            columns[pos].append(bit)

    top_column_parities = []
    bottom_column_parities = []
    for column in columns:
        top_column_parities.append(column[:numberOfRows // 2].count(1) % 2)
        bottom_column_parities.append(column[numberOfRows // 2:].count(1) % 2)
    if debugMode:
        print("     --- Top Parity ---")
        print(f"    {top_column_parities}")
        print("     --- Bottom Parity ---")
        print(f"    {bottom_column_parities}")
    return left_parities, right_parities, top_column_parities, bottom_column_parities