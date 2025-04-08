import math
N = int(input())

count = 0
for b in range(1,int(math.sqrt(N))):
    b_sqrt = b * b
    tmp = int(N / b_sqrt)
    print(tmp)
    while (tmp % 2 == 0):
        tmp /= 2
        print(tmp)
        count += 1
    
print(count)
