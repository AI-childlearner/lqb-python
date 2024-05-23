N = 100010
EPS = 1e-5

def check(x):
    global cow, n, m
    sum_arr = [0] * (n + 1)
    for i in range(1, n + 1):
        sum_arr[i] = sum_arr[i - 1] + (cow[i] - x)
    minv = 0
    for i in range(m, n + 1):
        minv = min(minv, sum_arr[i - m])
def merge_sort(l, r):
    if l == r:
        return 0
    mid = (l + r) // 2
    ans = merge_sort(l, mid) + merge_sort(mid + 1, r)
    i, j, k = l, mid + 1, 0
    while i <= mid and j <= r:
        if a[i] <= a[j]:
            tmp[k] = a[i]
            k += 1
            i += 1
        else:
            tmp[k] = a[j]
            k += 1
            j += 1
            ans += mid - i + 1
    while i <= mid:
        tmp[k] = a[i]
        k += 1
        i += 1
    while j <= r:
        tmp[k] = a[j]
        k += 1
        j += 1
    for i in range(l, r + 1):
        a[i] = tmp[i - l]
    return ans

while True:
    n = int(input())
    if n == 0:
        break
    a = list(map(int, input().split()))
    tmp = [0] * n
    print(merge_sort(0, n - 1))
        if sum_arr[i] - minv >= 0:
            return True
    return False

n, m = map(int, input().split())
cow = [0] * (N + 1)
l, r = 0, 0
for i in range(1, n + 1):
    cow[i] = int(input())
    r = max(r, cow[i])

while r - l > EPS:
    mid = (l + r) / 2
    if check(mid):
        l = mid
    else:
        r = mid

print(int(r * 1000))
