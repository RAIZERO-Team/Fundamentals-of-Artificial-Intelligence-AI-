# Author mohamed khalifa

def break_number(n, numbers):
    max_divisions = 0
    for num in numbers:
        divisions = 0
        while num % 2 == 0:
            num //= 2
            divisions += 1
        max_divisions = max(max_divisions, divisions)
    return max_divisions

n = int(input())
numbers = list(map(int, input().split()))
print(break_number(n, numbers))










