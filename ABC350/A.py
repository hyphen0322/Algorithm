S = list(input())

num = ''.join(S[3:])
num = int(num)
if 1 <= num < 350 and num != 316:
    print("Yes")
else:
    print("No")