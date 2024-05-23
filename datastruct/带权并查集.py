def find(x, p, d):
    if p[x] != x:
        rx = find(p[x], p, d)
        d[x] += d[p[x]]
        p[x] = rx
    return p[x]

def main():
    N = 30010
    n = 30000
    p = [i for i in range(N)]
    d = [0] * N
    s = [1] * N

    m = int(input())
    for _ in range(m):
        op, a, b = input().split()
        a, b = int(a), int(b)
        ra = find(a, p, d)
        rb = find(b, p, d)
        if op == 'M':
            if ra != rb:
                p[ra] = rb
                d[ra] = s[rb]
                s[rb] += s[ra]
        else:
            if ra != rb:
                print("-1")
            else:
                print(max(0, abs(d[a] - d[b]) - 1))

if __name__ == "__main__":
    main()
