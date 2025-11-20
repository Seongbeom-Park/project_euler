# Problem 1: Multiples of 3 or 5

# Solution 1
# iterate from 1 to 999 and check if the number is divisible by 3 or 5
def solve():
    total = 0
    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

# Solution 2
# let M_k be the set of multiples of k below limit
# M_15 = M_3 \cup M_5
# let S_k be the sum of elements in M_k
# S_15 = S_3 + S_5 - S_15
def SumMultiples(limit, multiples):
    n = (limit - 1) // multiples
    return multiples * (n * (n + 1)) // 2

def solve2():
    limit = 1000
    return SumMultiples(limit, 3) + SumMultiples(limit, 5) - SumMultiples(limit, 15)

# NOTE: computational complexity comparison
# Let n be the limit number, m be the number of factors
# solution 1 has O(n * m)
# solution 2 has O(2**m)

if __name__ == "__main__":
    result = solve()
    print(result)
    # Expected output: 233168
    result2 = solve2()
    print(result2)
    # Expected output: 233168
