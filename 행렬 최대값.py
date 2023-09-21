matrix = []
max_row = []
row_number = []
max_column = []
column_n = []
for i in range(9):
    n = list(map(int, input().split()))
    matrix.append(n)

for i in range(len(matrix)):
    max_row.append(max(matrix[i]))
    row_number.append(matrix[i].index(max(matrix[i])))
    for j in range(len(matrix)):
        max_column = max(max_row)
        a = max_row.index(max(max_row))
        column_n = row_number[a]

print(max_column)
print((max_row.index(max(max_row)) + 1), end = ' ')
print((column_n + 1))







