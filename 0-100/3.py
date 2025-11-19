# Problem 3: Largest Prime Factor

# Solution 1
# find the largest prime factor of 600851475143 by trial division
def solve():
    n = 600851475143
    factor = 2
    last_factor = 1
    while n > 1:
        if n % factor == 0:
            last_factor = factor
            n //= factor
            while n % factor == 0:
                n //= factor
        factor += 1
    return last_factor

# Solution 2
# skip even factors except 2
def solve2():
    n = 600851475143
    factor = 2
    last_factor = 1
    while n > 1:
        if n % factor == 0:
            last_factor = factor
            n //= factor
            while n % factor == 0:
                n //= factor
        factor += 1 if factor == 2 else 2
    return last_factor

# Solution 3
# maximum factor can be at most sqrt(n)
def solve3():
    n = 600851475143
    factor = 2
    last_factor = 1
    max_factor = int(n**0.5)
    while n > 1:
        if n % factor == 0:
            last_factor = factor
            n //= factor
            while n % factor == 0:
                n //= factor
        factor += 1 if factor == 2 else 2
        if factor > max_factor:
            if n > 1:
                last_factor = n
                break
    return last_factor

if __name__ == "__main__":
    result = solve()
    print(result)
    # Expected output: 6857
    result2 = solve2()
    print(result2)
    # Expected output: 6857
    result3 = solve3()
    print(result3)
    # Expected output: 6857
