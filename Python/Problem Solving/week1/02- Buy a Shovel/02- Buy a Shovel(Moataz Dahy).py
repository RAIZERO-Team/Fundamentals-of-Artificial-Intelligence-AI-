'''Moataz Dahy'''

A, B = map(int, input().split())

for i in range(1, 11):
  if (A * i) % 10 == 0 or (A * i) % 10 == B :
    print(i)
    break