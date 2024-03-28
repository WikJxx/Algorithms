def sieveOfEratosthenes(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False
    p = 2
    while (p*p <= n):
        if primes[p]:
            for i in range(p*p, n+1, p):
                primes[i] = False
        p += 1
    return primes