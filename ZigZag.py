def convert(s: str, numRows: int) -> str:
    matrix = []
    rowCount = 0
    pos = 0
    while pos < len(s):
        # print (pos)
        if rowCount % (numRows - 1) == 0:
            list_temp = [c for c in s[pos : pos + numRows]]
            matrix.append(list_temp)
            pos += numRows
        else:
            leading_spaces = [" " for i in range(numRows - rowCount - 1)]
            lagging_spaces = [" " for i in range(rowCount)]
            list_temp = leading_spaces + [s[pos]] + lagging_spaces
            matrix.append(list_temp)
            pos += 1
        rowCount += 1
        if rowCount == numRows - 1:
            rowCount = rowCount // numRows
    for row in matrix:
        if len(row) < numRows:
            list_temp = [" " for i in range(numRows - len(row))]
            row = row + list_temp
            matrix[-1] = row
    t_matrix = zip(*matrix)
    s = ""
    for row in t_matrix:
        for el in row:
            if el != " ":
                s += el
    return s


def main():
    convert("PAYPALISHIRING", 3)


if __name__ == "__main__":
    main()
