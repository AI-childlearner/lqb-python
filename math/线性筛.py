N = 1000010
primes = []
is_prime = [True] * N

def get_primes(n):
    global primes
    is_prime[1] = False
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
        j = 1
        while j <= len(primes) and primes[j - 1] * i <= n:
            is_prime[primes[j - 1] * i] = False
            if i % primes[j - 1] == 0:
                break
            j += 1

def main():
    get_primes(N - 1)
    while True:
        n = int(input())
        if n == 0:
            break
        for p in primes:
            if is_prime[n - p]:
                print(f"{n} = {p} + {n - p}")
                break

if __name__ == "__main__":
    main()
