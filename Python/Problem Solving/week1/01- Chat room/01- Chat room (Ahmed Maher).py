# Author : Ahmed Maher

x = input()
z = list("hello")
count = 0

for char in x:
    if char == z[count]:
        count += 1
    if count == len(z):
        print("YES")
        break
else:
    print("NO")