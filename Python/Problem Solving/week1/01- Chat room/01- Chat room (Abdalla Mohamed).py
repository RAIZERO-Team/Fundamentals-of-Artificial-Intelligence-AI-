s=input()
word="hello"
c=0
for i in s:
    if i==word[c]:
        c+=1
    if c==len(word):
        print("YES")
        break
else:
        print("NO")        

