S = list(input())
T = list(input())
moji = []
index = 0
for i in range(len(T)):
    if S[index] == T[i]:
        moji.append(str(i+1))
        index += 1
print(" ".join(moji))