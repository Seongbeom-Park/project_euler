# Problem 5: Smallest Multiple
# lcm of 1 to 20
import math
def solve():
    return math.lcm(*range(1, 21))

# Solution
# find maximum numbers that consist of power of a prime number
def find_primes(n):
    prime_numbers = []
    i = 2
    while i <= n:
        is_prime = True
        for p in prime_numbers:
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers += [i]
        i += 1
    return prime_numbers

def solve_1():
    n = 20
    prime_numbers = find_primes(20)
    answer = 1
    for p in prime_numbers:
        k = 1
        while p ** (k + 1) <= n:
            k += 1
        answer *= p**k
    return answer

# NOTE: lcm(a, b, ..., x) = lcm(a, lcm(b, ..., x))
# lcm(a, b) = a * b / gcd(a, b)
def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while b > 0:
        a, b = b, a % b
    return a
def _lcm(a, b):
    return a * b // gcd(a, b)
def lcm(numbers):
    if len(numbers) == 2:
        return _lcm(numbers[0], numbers[1])
    a, b = numbers[0], lcm(numbers[1:])
    return a * b // gcd(a, b)
def solve_2():
    return lcm(list(range(1, 21)))

if __name__ == '__main__':
    result = solve()
    print(result)
    # Expected output: 232792560
    resule_1 = solve_1()
    print(resule_1)
    resule_2 = solve_2()
    print(resule_2)
