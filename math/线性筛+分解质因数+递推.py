MOD = int(1e9 + 7)

def get_primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    primes = []
    
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
        for prime in primes:
            if prime * i > n:
                break
            is_prime[prime * i] = False
            if i % prime == 0:
                break
    return primes, is_prime

def main():
    n = int(input())
    primes, is_prime = get_primes(n)
    
    ans = 1
    for i in range(2, n + 1):
        if not is_prime[i]:
            continue
        res = 0
        j = i
        while j <= n:
            res += n // j
            j *= i
        ans = ans * (res * 2 + 1) % MOD
    
    print(ans)

if __name__ == "__main__":
    main()
