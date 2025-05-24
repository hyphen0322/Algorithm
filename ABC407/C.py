from collections import deque

S = input().strip()

def min_button_presses(S):
    visited = set()
    queue = deque()
    queue.append(("", 0))

    while queue:
        t, steps = queue.popleft()

        if t == S:
            return steps
        
        if len(t) > len(S):
            continue

        t1 = t + "0"
        if t1 not in visited:
            visited.add(t1)
            queue.append((t1, steps + 1))

        if t:
            t2 = ''.join(str((int(c) + 1) % 10) for c in t)
            if t2 not in visited:
                visited.add(t2)
                queue.append((t2, steps + 1))

    return -1

print(min_button_presses(S))
