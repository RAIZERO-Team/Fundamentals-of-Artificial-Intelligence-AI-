s = input()
s_list = list(s)
i, j = 0, len(s) - 1
while i <= j:
    if s_list[i] == s_list[j] == '?':
        s_list[i] = s_list[j] = 'a'
    elif s_list[i] == '?':
        s_list[i] = s_list[j]
    elif s_list[j] == '?':
        s_list[j] = s_list[i]
    elif s_list[i] != s_list[j]:
        print(-1)
        break
    i += 1
    j -= 1
else:
    print(''.join(s_list))