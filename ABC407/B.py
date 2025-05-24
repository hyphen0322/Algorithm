X,Y = map(int,input().split())
count = 0
diff = 0
total = 0
for i in range(6):
    for j in range(6):
        a = i + 1
        b = j + 1
        total = a + b
        diff = abs(a - b)
        if total >= X or diff >= Y:
            count += 1
ans = count / 36

        
print(ans)