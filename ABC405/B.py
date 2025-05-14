N, M = map(int, input().split())
A = list(map(int, input().split()))
required = set(range(1, M + 1))
count = 0

for i in range(N - 1, -1, -1):
    current = set(A[:i + 1])
    if not required.issubset(current):
        break
    count += 1

print(count)
