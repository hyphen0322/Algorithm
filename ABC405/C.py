N = int(input())
A = list(map(int, input().split()))
ans = 0
sum = sum(A)

for i in range(N):
    sum -= A[i]
    ans += A[i] * sum

print(ans)