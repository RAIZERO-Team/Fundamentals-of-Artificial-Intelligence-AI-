# Author : Ahmed Maher

n = int(input())
numbers = map(int, input().split())
maxNum = 0

for num in numbers:
    count = 0
    while num % 2 == 0:
        num //= 2
        count += 1
    if count > maxNum:
        maxNum = count

print(maxNum)