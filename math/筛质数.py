N = 100010
n = int(input())
primes = [0]
is_prime = [True] * N
def get_primes(n):

    is_prime[1] = False
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
        for j in range(1,n):
            if primes[j] * i > n:
                break
            is_prime[primes[j] * i] = False
            if i % primes[j] == 0:
                break
get_primes(n + 1)

if n <= 2:
    print("1")
else:
    print("2")

for i in range(2, n + 2):
    if is_prime[i]:
        print("1")
    else:
        print("2", end=' ')
print()
