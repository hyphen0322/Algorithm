N = int(input())
A = list(map(int, input().split()))

# 1からNまでの順列
target = list(range(1, N + 1))
count = 0
swaps = []

for i in range(N):
    # 正しい値が A[i] にない場合
    while A[i] != target[i]:
        # A[i] が正しい位置（A[i] - 1）に移動する
        correct_index = A[i] - 1
        
        # 交換の記録（1始まりのインデックスにする）
        swaps.append(f'{i + 1} {correct_index + 1}')
        
        # A[i] と A[correct_index] を入れ替える
        A[i], A[correct_index] = A[correct_index], A[i]
        count += 1

# 交換回数を先に出力
print(count)

# 交換の詳細を出力
for swap in swaps:
    print(swap)
