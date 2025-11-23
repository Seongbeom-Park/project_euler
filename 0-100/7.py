# Problem 7: 10 001st Prime

# iterate numbers and check is dividable by primes
def solve():
    primes = []
    n = 2
    while len(primes) < 10001:
        is_prime = True
        for p in primes:
            if n % p == 0:
                is_prime = False
            if not is_prime:
                break
        if is_prime:
            primes += [n]
        n += 1
    return primes[-1]

# iterate primes p < sqrt(n)
def solve_2():
    primes = []
    n = 2
    while len(primes) < 10001:
        is_prime = True
        for p in primes:
            if p > n**1/2:
                break
            if n % p == 0:
                is_prime = False
            if not is_prime:
                break
        if is_prime:
            primes += [n]
        n += 1
    return primes[-1]

# iterate odd-number only
def solve_3():
    primes = [2]
    n = 3
    while len(primes) < 10001:
        is_prime = True
        for p in primes:
            if p > n**1/2:
                break
            if n % p == 0:
                is_prime = False
            if not is_prime:
                break
        if is_prime:
            primes += [n]
        n += 2
    return primes[-1]

# prime number is (6k + 1) or (6k + 5)
# 6k     % 2 = 0
# 6k + 1
# 6k + 2 % 2 = 0
# 6k + 3 % 3 = 0
# 6k + 4 % 2 = 0
# 6k + 5
def solve_4():
    primes = [2, 3, 5]
    k = 6
    while len(primes) < 10001:
        n = k + 1
        is_prime = True
        for p in primes:
            if p > n**1/2:
                break
            if n % p == 0:
                is_prime = False
            if not is_prime:
                break
        if is_prime:
            primes += [n]

        n = k + 5
        is_prime = True
        for p in primes:
            if p > n**1/2:
                break
            if n % p == 0:
                is_prime = False
            if not is_prime:
                break
        if is_prime:
            primes += [n]

        k += 6

    return primes[10000]

if __name__ == '__main__':
    print(solve())
    # Expected Output: 104743
    print(solve_2())
    print(solve_3())
    print(solve_4())
