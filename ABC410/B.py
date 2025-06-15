N, Q = map(int, input().split()) 
X = list(map(int, input().split()))  

ball_counts = [0] * (N + 1)
result = []

for x in X:
    if x >= 1:
        ball_counts[x] += 1
        result.append(x)
    else:
        min_index = min(range(1, N + 1), key=lambda i: ball_counts[i])
        ball_counts[min_index] += 1
        result.append(min_index)

print(" ".join(map(str, result)))  
