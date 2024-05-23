import collections

adjvex = collections.defaultdict(list)
global match
match = []
global visited
visited = []

def dfs(x: int) -> bool:
    for y in adjvex[x]:
        if visited[y] == False:
            visited[y] = True
            if match[y] == -1 or dfs(match[y]) == True:
                match[y] = x
                return True
    return False


def main():
    global match
    global visited

    while True:
        tmp = input().split()
        if len(tmp) == 1:
            break
        n, m, K = map(int, tmp)
        a = [-1 for _ in range(K)]
        b = [-1 for _ in range(K)]

        for i in range(K):
            ii, ai, bi = map(int, input().split())
            a[i] = ai
            b[i] = bi

        adjvex.clear()
        for x, y in zip(a, b):
            if x == 0 or y == 0:
                continue
            adjvex[x].append(y)

        match = [-1 for _ in range(m)]

        res = 0
        for x in range(n):
            visited = [False for _ in range(m)]
            if dfs(x) == True:
                res += 1
        print(res)

if __name__ == "__main__":
    main()
