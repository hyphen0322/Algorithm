N, Q = map(int,input().split())
T = list(map(int,input().split()))
teeth = [1] * N 
count = N
for i in range(Q):
    index = T[i] - 1 
    if teeth[index] == 1:
        teeth[index] = 0
        count -= 1
    else:
        teeth[index] = 1
        count += 1
print(count)