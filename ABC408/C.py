from collections import defaultdict

N, M = map(int, input().split())

# 各位置に関わるイベントのリストを入れる
events = defaultdict(list)

for i in range(M):
    L, R = map(int, input().split())
    events[L].append(('start', i))
    events[R+1].append(('end', i))

battery = {i: [] for i in range(1, N+1)}  # 1〜N 各位置のイベントリスト
active = set()

for pos in range(1, N+1):
    for op, idx in events[pos]:
        if op == 'start':
            active.add(idx)
        elif op == 'end':
            active.discard(idx)
    battery[pos] = list(active)

# チェック
if any(len(battery[i]) == 0 for i in range(1, N+1)):
    print("0")
else:
    min_count = min(len(battery[i]) for i in range(1, N+1))
    print(min_count)
