'''Moataz Dahy'''


word = list("hello")
s = input()
count = 0

for i in s:
    if i == word[count]:
        count += 1
    if count == len(word):
        print("YES")
        break
else:
    print("NO")