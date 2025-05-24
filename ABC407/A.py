A,B = map(int,input().split())
ans = (A / B)
ans_int = int(ans)
if ans == 0:
    print("1")
else:
    if (ans - ans_int) >= 0.5:
        print(ans_int+1)
    else:
        print(ans_int)