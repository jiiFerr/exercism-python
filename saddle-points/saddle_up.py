# matrix = [[9, 8, 7], [5, 3, 2], [6, 6, 7]]
matrix = [[4, 5, 4], [3, 5, 5], [1, 5, 4]]
print("Matrix:")
print(matrix)
print()

columns = []
for col_num in range(len(matrix[0])):
    columns.append([row[col_num] for row in matrix])
print("Matrix by columns: ")
print(columns)
print()

len_set = len(set([len(row) for row in matrix]))
print(len_set)


saddle_points = []
for row_num, row in enumerate(matrix):
    for col_num, value in enumerate(row):
        if ( value == max(row) == max(columns[col_num])):
            saddle_points.append({"row": int(row_num + 1), "column": int(col_num + 1)})

print(saddle_points)
