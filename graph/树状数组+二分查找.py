class BitTree:
    def __init__(self, n: int):
        self.n = n
        self.tree = [0 for _ in range(n + 1)]

    def lowbit(self, x: int) -> int:
        return x & (-x)

    def add(self, i: int, val: int) -> None:
        while i <= self.n:
            self.tree[i] += val
            i += self.lowbit(i)

    def query(self, i: int) -> int:
        res = 0
        while 1 <= i:
            res += self.tree[i]
            i -= self.lowbit(i)
        return res


def main():
    n = int(input())
    A = [0 for _ in range(n + 1)]
    A[1] = 0
    for i in range(2, n + 1):
        A[i] = int(input())

    BT = BitTree(n)
    for i in range(1, n + 1):
        BT.add(i, 1)

    res = [0 for _ in range(n + 1)]
    for i in range(n, 0, -1):
        cur = A[i] + 1
        l = 1
        r = n
        while l < r:
            mid = l + r >> 1
            if BT.query(mid) >= cur:
                r = mid
            else:
                l = mid + 1
        res[i] = l
        BT.add(l, -1)

    for i in range(1, n + 1):
        print(res[i])


if __name__ == "__main__":
    main()

