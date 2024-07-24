'''Moataz Dahy'''

n, k = map(int, input().split())

count = 0

for i in range(n):
  numbers = input()
  if all(str(digit) in numbers for digit in range(k + 1)) :
    count += 1

print(count)