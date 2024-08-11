# Author : mohamed khalifa

s = list(input())
length = len(s)
palindrome_possible = True

for i in range(length // 2):
    j = length - i - 1
    
    if s[i] == s[j] == '?':
        s[i] = s[j] = 'a'
    
    elif s[i] == '?':
        s[i] = s[j]
    
    elif s[j] == '?':
        s[j] = s[i]
    
    elif s[i] != s[j]:
        palindrome_possible = False
        break

if length % 2 == 1 and s[length // 2] == '?':
    s[length // 2] = 'a'

if palindrome_possible:
    print("".join(s))
else:
    print(-1)
