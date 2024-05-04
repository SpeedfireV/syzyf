from table_display_8x8 import create_table


def check_table_parity(data, numberOfRows,debugMode):
    new_data = []
    for i in range(numberOfRows):
        for column in data:
            new_data.append(column[i])
    data = new_data
    rows: list[list[int]] = create_table(data, numberOfRows)
    columns = [[] for i in range(8)]
    row_parities = []
    for row in rows:
        row_parity = row.count(1) % 2
        row_parities.append(row_parity)
        if debugMode:
            print(f"{row_parity} | {row}")
        for pos, bit in enumerate(row):
            columns[pos].append(bit)

    top_column_parity = []
    bottom_column_parity = []
    for column in columns:
        top_column_parity.append(column[0:numberOfRows // 2].count(1) % 2)
        bottom_column_parity.append(column[numberOfRows // 2:].count(1) % 2)
    if debugMode:
        print("     --- Top Column Parity ---")
        print(f"    {top_column_parity}")
        print("     --- Bottom Column Parity ---")
        print(f"    {bottom_column_parity}")
    return row_parities, top_column_parity, bottom_column_parity