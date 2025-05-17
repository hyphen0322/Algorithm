def solve():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0

    for l in range(n - 3):
        for r in range(l + 3, n):
            sub_array = p[l : r + 1]
            m = len(sub_array)

            if sub_array[0] < sub_array[1]:
                peak_count = 0
                valley_count = 0

                for i in range(1, m - 1):
                    if sub_array[i - 1] < sub_array[i] > sub_array[i + 1]:
                        peak_count += 1
                    if sub_array[i - 1] > sub_array[i] < sub_array[i + 1]:
                        valley_count += 1

                if peak_count == 1 and valley_count == 1:
                    count += 1

    print(count)

if __name__ == "__main__":
    solve()
