S = input().strip()
T = input().strip()

ans_list = []
for i in range(1,len(S)):
    if S[i].isupper() == True:
        if S[i-1] in T:
            ans_list.append(S[i-1])
            
print(ans_list)