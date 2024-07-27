# Author : Ahmed Maher

k, c = map(int, input().split())

for i in range(1, 11):
    result = (k * i) 
    if result % 10 == 0 or result % 10 == c:
        print(i)
        break