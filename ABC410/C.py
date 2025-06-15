from collections import deque

N, Q = map(int, input().split())
query = [list(map(int, input().split())) for _ in range(Q)]

result = deque(range(1, N + 1))

for q in query:
    if q[0] == 1:
        result[q[1] - 1] = q[2]
    elif q[0] == 2:
        print(result[q[1] - 1])
    elif q[0] == 3:
        result.rotate(-q[1])  
