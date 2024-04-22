

def get_columns(data):
    columns = []

    for pos, bit in enumerate(data):
        if len(columns) < pos % 8 + 1:
            columns.append([bit])
        else:
            columns[pos % 8].append(bit)

    return columns

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



