f1 = open('B_prime_subtractorization_input.txt', 'r')
f2 = open('B_prime_subtractorization_output.txt', 'w')


def prime_list(n):
    sieve = [True] * (n+1)

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i]:
            for j in range(i + i, n+1, i):
                sieve[j] = False

    return [i for i in range(2, n+1) if sieve[i]]


input = f1.readline
print = f2.write
T = int(input())
for test in range(1, T+1):
    N = int(input())
    primes = prime_list(N)
    s = set(primes)

    tmp = [2] if N >= 5 else []
    n = len(primes)
    for a in range(n):
        if primes[a] - 2 in s:
            tmp.append(primes[a] - 2)

    ans = len(set(tmp))
    print(f"Case #{test}: {ans}\n")

f1.close()
f2.close()