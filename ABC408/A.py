N,S = map(int, input().split())
T = list(map(int,input().split()))
awake = True
tmp = 0
if T[0] > S:
    awake = False
for i in range(1,N):
    sleep = T[i] - T[i-1]
    #print(sleep)
    num = S + 0.5
    if sleep >= num:
        awake = False
if awake == True:
    print("Yes")
else:
    print("No")
    