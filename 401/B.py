
num = int(input())
S = []
key = 0
error = 0
for i in range(num):
    user_input = input()
    S.append(user_input)
    if (S[i] == "login" and key == 0):
        key += 1
    if (S[i] == "logout" and key == 1):
        key = 0
    if (S[i] == "private" and key == 0):
        error += 1

print(error)