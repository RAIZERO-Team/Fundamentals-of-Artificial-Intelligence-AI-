# Author : Moataz Dahy
S = list(input())
length = len(S)
i = 0
j = length - 1
while i < j:
      if S[i] == S[j] == '?':
          S[i] = S[j] = 'a'
    
      elif S[i] == '?':
          S[i] = S[j]
          
      elif S[j] == '?':
          S[j] = S[i]
          
      elif S[i] != S[j]:
          print(-1)
          break
      
      i += 1
      j -= 1
else:
      if length % 2 == 1 and S[length // 2] == '?':
          S[length // 2] = 'a'
      print(''.join(S))
