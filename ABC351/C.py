N = int(input())
A = list(map(int, input().split()))
balls = []

for i in range(N):
    # ボールの大きさは 2^A[i]
    balls.append(2 ** A[i])
    
    # 連結できる限り繰り返す
    while len(balls) > 1 and balls[-1] == balls[-2]:
        # 2つのボールを合成
        new_value = balls[-1] + balls[-2]
        # 2つのボールを取り除く
        balls.pop()
        balls.pop()
        # 合成したボールを追加
        balls.append(new_value)

print(len(balls))
