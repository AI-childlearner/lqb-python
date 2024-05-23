a, b, p=int(input()), int(input()), int(input())
ans = 0
while b:
    if b & 1:
        ans = (ans + a) % p
    a = (a << 1) % p
    b >>= 1
print(ans)
