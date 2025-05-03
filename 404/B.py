N = int(input())
S = [list(input()) for _ in range(N)]
T = [list(input()) for _ in range(N)]

def rotate_90(grid):
    return [list(row) for row in zip(*grid[::-1])]

def count_changes(S, T):
    changes = 0
    for i in range(N):
        for j in range(N):
            if S[i][j] != T[i][j]:
                changes += 1
    return changes

min_changes = float('inf')

for rotations in range(4):
    changes = count_changes(S, T)
    min_changes = min(min_changes, changes + rotations)
    S = rotate_90(S)

print(min_changes)
