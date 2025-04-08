N, M = map(int,input().split())
num = 1
for i in range(1,M+1):
    num += N ** i

if num <= 10**9:
    print(num)
else:
    print("inf")

