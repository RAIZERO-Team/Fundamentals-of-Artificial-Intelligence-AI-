# mohamed khalifa

k , r = map(int , input().split()) ; shovels = 1
while((shovels * k ) % 10  not in (0 , r)) : 
    shovels+=1
print(shovels)
