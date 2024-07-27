'''Moataz Dahy'''

n, m, k = map(int, input().split())
List = [list(map(int, input().split())) for _ in range(n)]

rows = list(range(n))
columns = list(range(m))

for _ in range(k):  
    s, x, y = input().split()
    x, y = int(x) - 1, int(y) - 1
    
    if s == 'g':
        print(List[rows[x]][columns[y]])
    elif s == 'r':
        rows[x], rows[y] = rows[y], rows[x]  
    elif s == 'c':
        columns[x], columns[y] = columns[y], columns[x]
    

