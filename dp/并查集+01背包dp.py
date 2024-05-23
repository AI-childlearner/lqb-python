def find(x, ori):
    if x != ori[x]:
        ori[x] = find(ori[x], ori)
    return ori[x]

def merge(x, y, ori, price, val):
    pr = find(x, ori)
    nx = find(y, ori)
    if pr == nx:
        return
    ori[pr] = nx
    price[nx] += price[pr]
    val[nx] += val[pr]

def main():
    n, m, w = map(int, input().split())
    ori = list(range(n + 1))
    price = [0] * (n + 1)
    val = [0] * (n + 1)
    dp = [0] * (w + 1)
    for i in range(1, n + 1):
        price[i], val[i] = map(int, input().split())

    for i in range(m):
        u, v = map(int, input().split())
        merge(u, v, ori, price, val)

    for i in range(1, n + 1):
        if i != ori[i]:
            continue
        for j in range(w, price[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - price[i]] + val[i])

    print(dp[w])

if __name__ == "__main__":
    main()
