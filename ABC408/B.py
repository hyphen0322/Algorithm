N = int(input())
A = list(map(int, input().split()))
A_set = set(A)

print(len(A_set))
print(" ".join(map(str, sorted(A_set))))