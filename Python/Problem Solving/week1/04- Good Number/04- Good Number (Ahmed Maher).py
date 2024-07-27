# Author : Ahmed Maher

size, range_val = map(int, input().split())
result = 0
myRange = "0123456789"

for i in range(size):
    counter = 0
    num = input()
    for z in range(range_val + 1):
        if myRange[z] in num:
            counter += 1
    if counter == range_val + 1:
        result += 1

print(result)