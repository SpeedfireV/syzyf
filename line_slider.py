def slide_lines(columns, number_of_rows):
    final_columns = []
    if len(columns[0]) == 8:
        for pos, column in enumerate(columns):
            new_column = column[::1]

            new_column.extend([0 for _ in range(number_of_rows - 8)])
            columns[pos] = new_column
    for pos, column in enumerate(columns):
        jump = pos * 2
        new_poses = []
        for i in range(len(column)):
            if i + jump > len(column) - 1:
                new_poses.append(jump - (len(column) - i))
            else:
                new_poses.append(i + jump)
        new_column = [0 for _ in range(number_of_rows)]
        for i, new_pos in enumerate(new_poses):
            new_column[new_pos] = column[i]
        final_columns.append(new_column)
    return final_columns
