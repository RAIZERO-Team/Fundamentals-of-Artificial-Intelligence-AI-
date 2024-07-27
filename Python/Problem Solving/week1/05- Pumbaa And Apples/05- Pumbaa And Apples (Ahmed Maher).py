# Author : Ahmed Maher

row, column, process = map(int, input().split())
arr = [[0] * (column + 1)] + [[0] + list(map(int, input().split())) for _ in range(row)]
arrR, arrC = list(range(row + 1)), list(range(column + 1))
output = []

for _ in range(process):
    c, num1, num2 = input().split()
    num1, num2 = int(num1), int(num2)
    if c == 'g':
        output.append(arr[arrR[num1]][arrC[num2]])
    elif c == 'r':
        arrR[num1], arrR[num2] = arrR[num2], arrR[num1]
    elif c == 'c':
        arrC[num1], arrC[num2] = arrC[num2], arrC[num1]

print('\n'.join(map(str, output)))