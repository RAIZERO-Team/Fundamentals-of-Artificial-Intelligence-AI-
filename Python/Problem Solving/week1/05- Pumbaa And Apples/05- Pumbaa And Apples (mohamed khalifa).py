# # Author mohamed khalifa

n, m, k = map(int, input().split())
list_2d = [list(map(int, input().split())) for _ in range(n)]

rows = list(range(n))
cols = list(range(m))

for _ in range(k):
    s, x, y = input().split()
    x, y = int(x) - 1, int(y) - 1

    if s == 'g':
        print(list_2d[rows[x]][cols[y]])
    elif s == 'c':
        cols[x], cols[y] = cols[y], cols[x]
    elif s == 'r':
        rows[x], rows[y] = rows[y], rows[x]      

        
