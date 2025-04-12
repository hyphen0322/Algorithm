
N, K = map(int, input().split())
MOD = 10**9
A = [1] * K

sum_no = sum(A)

for i in range(K, N+1):
    A.append(sum_no % MOD)
    # 部分合計を更新
    sum_no = (sum_no - A[i-K] + A[i]) % MOD

ans = A[N] % MOD
print(ans)
