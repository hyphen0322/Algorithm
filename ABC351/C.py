N = int(input())
A = list(map(int, input().split()))
for i in range(N):
    if A[-1] == A[-2]:
        sum = A[-1] + A[-2]
        A.pop(-1)
        A.pop(-1)
        A.append(sum)

