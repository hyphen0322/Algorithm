N, K = map(int, input().split())
A = list(map(int, input().split()))
num = 1
for i in range(N):
    num = num * A[i]
    if num >= 10**K:
        num = 1

print(num)