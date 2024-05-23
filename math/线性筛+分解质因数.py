def get_primes(n):
    primes = []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
        for prime in primes:
            if i * prime > n:
                break
            is_prime[i * prime] = False
            if i % prime == 0:
                break
    return primes

if __name__ == "__main__":
    n = int(input())
    primes = get_primes(n)
    for i in range(2, n + 1):
        if i not in primes:
            continue
        ans = 0
        j = i
        while j <= n:
            ans += n // j
            j *= i
        if ans:
            print(i, ans)
