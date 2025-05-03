import string
S = input()
for c in string.ascii_lowercase:
        if c not in S:
            print(c)
            break
