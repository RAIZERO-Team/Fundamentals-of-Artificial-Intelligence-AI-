# Author mohamed khalifa

N  , K = map(int , input().split())
string = ''.join(map(str, range(1, K + 1))) + "0"
good_numbers= 0 
for _ in range(N) : 
    numbers = input()
    isGood = True
    for i in range(K+1) :
        if str(i) not in numbers :  
            isGood = False
    good_numbers += 1 if isGood else 0

print(good_numbers)        
