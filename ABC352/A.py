N,X,Y,Z = map(int, input().split())
if X < Y:
    if X < Z and Z < Y:
        print("Yes")
    else:
        print("No")
else:
    if X > Z and Z > Y:
        print("Yes")
    else:
        print("No")
