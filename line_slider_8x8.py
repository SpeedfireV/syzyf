

def get_columns(data):
    columns = []

    for pos, bit in enumerate(data):
        if len(columns) < pos % 8 + 1:
            columns.append([bit])
        else:
            columns[pos % 8].append(bit)

    return columns

def get_data(columns):
    data = []
    for i in range(8):
        for column in columns:
            data.append(column[i])

    return data

def get_table_info(data):
    row_parities = []
    column_parities = []
    amount_of_ones = [] # >=2 na 4 pierwszych bitach >=2 na 4 ostatnich bitach
    # Rows
    for i in range(8):
        first_four = data[i* 8:(i + 1) * 8 - 4].count(1)
        one_count = data[i* 8:(i + 1) * 8].count(1)
        if first_four >= 2:
            amount_of_ones.append(1)
        else:
            amount_of_ones.append(0)
        if one_count - first_four >= 2:
            amount_of_ones.append(1)
        else:
            amount_of_ones.append(0)
        row_parities.append(data[i* 8:(i + 1) * 8].count(1) % 2)
    for i in range(8):
        column_bites = []
        for bit in data[i::8]:
            column_bites.append(bit)
        column_parities.append(column_bites.count(1) % 2)
    column_parities.append(-1)
    column_parities.extend(row_parities[::1])
    column_parities.append(-1)
    column_parities.extend(amount_of_ones[::1])
    return column_parities



def slide_lines(columns):
    final_columns = []
    for pos, column in enumerate(columns):
        jump = pos
        new_poses = []
        for i in range(len(column)):
            if i + jump > len(column) - 1:
                new_poses.append(jump - (len(column) - i))
            else:
                new_poses.append(i + jump)
        new_column = [0 for i in range(8)]
        for i, new_pos in enumerate(new_poses):
            new_column[new_pos] = column[i]
        final_columns.append(new_column)
    return final_columns



