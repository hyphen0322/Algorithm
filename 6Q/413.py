N = int(input())
S = [input() for _ in range(N)]

ans = set()
for i in S:
    for j in S:
        if i != j:
            ans.add(i+j)
print(len(ans))