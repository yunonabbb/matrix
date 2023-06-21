matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

for row in matrix:
    for element in row:
        print(element ** 2, end=" ")
    print()

matrix = []
for _ in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

for row in matrix:
    for element in row:
        print(element, end=" ")
    print()


rows = int(input("Введите количество строк: "))
columns = int(input("Введите количество столбцов: "))

matrix = []
for _ in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

for row in matrix:
    for element in row:
        print(element, end=" ")
    print()


rows = int(input("Введите количество строк: "))
columns = int(input("Введите количество столбцов: "))

matrix = []
for _ in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

total_sum = 0
for row in matrix:
    for element in row:
        total_sum += element

print("Сумма всех значений в матрице:", total_sum)



rows = int(input("Введите количество строк: "))
columns = int(input("Введите количество столбцов: "))

matrix = []
for _ in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

column_sums = [0] * columns
for row in matrix:
    for j, element in enumerate(row):
        column_sums[j] += element

print("Сумма значений по каждому столбцу:")
for column_sum in column_sums:
    print(column_sum)


rows = int(input("Введите количество строк: "))
columns = int(input("Введите количество столбцов: "))

matrix = []
for _ in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

row_sums = []
for row in matrix:
    row_sum = sum(row)
    row_sums.append(row_sum)

print("Сумма значений по каждой строке:")
for row_sum in row_sums:
    print(row_sum)


rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

matrix = []

for _ in range(rows):
    row = []
    for _ in range(cols):
        value = int(input("Введите значение: "))
        row.append(value)
    matrix.append(row)

primary_diagonal_sum = 0
secondary_diagonal_sum = 0

for i in range(rows):
    for j in range(cols):
        if i == j:
            primary_diagonal_sum += matrix[i][j]
        if i + j == rows - 1:
            secondary_diagonal_sum += matrix[i][j]

print("Сумма значений по главной диагонали:", primary_diagonal_sum)
print("Сумма значений по побочной диагонали:", secondary_diagonal_sum)



rows = 10
cols = 10

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            row.append("*")
        else:
            row.append(" ")
    matrix.append(row)

for row in matrix:
    for symbol in row:
        print(symbol, end=' ')
    print()















