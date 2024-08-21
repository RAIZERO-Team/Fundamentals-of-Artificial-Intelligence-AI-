def prime(N):
    if N <= 1:
        return False
    for k in range(2, int(N ** 0.5) + 1):
        if N % k == 0:
            return False
    return True

T = int(input())

for i in range(T):
    N = int(input())
    
    fib_sequence = [0, 1]
    
    for j in range(2, N + 1):
        fib_sequence.append(fib_sequence[j-1] + fib_sequence[j-2])
    
    number = fib_sequence[N]
    
    if prime(number):
        print("prime")
    else:
        print("not prime")
