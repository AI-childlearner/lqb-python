N = 1010
a = [0, 10, 20, 50, 100]
f = [0] * N

n = int(input())

f[0] = 1
for i in range(1, 5):
    for j in range(a[i], n + 1):
        f[j] += f[j - a[i]]

print(f[n])
