A,B,C,D = map(int, input().split())
if A > C or (A == C and B > D):
    print('Yes')
else:
    print('No')
