N = int(input())
sholder = 0
head = 0
for i in range(N):
    A,B = map(int, input().split())
    length = B - A
    if length - head > 0:
        head = length
    sholder += A

print(sholder + head)