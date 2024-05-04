def create_table(data, numberOfRows):
    rows = []
    for i in range(numberOfRows):
        rows.append(data[i * 8:(i + 1) * 8])
    return rows
