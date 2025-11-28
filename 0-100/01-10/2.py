# Problem 2: Even Fibonacci Numbers

# Solution 1
# generate Fibonacci sequence and sum even-valued terms until the sequence value not exceeds four million
def solve():
    a, b = 1, 2
    total = 0
    while a <= 4000000:
        if a % 2 == 0:
            total += a
        a, b = b, a + b
    return total

# Solution 2
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# Even Fibonacci numbers are at 3k-1 positions
# fib(2) = 2, fib(5) = 8
# for k >= 3, fib(3k-1) = fib(3k-2) + fib(3k-3)
#                       = fib(3k-3) + fib(3k-4) + fib(3k-4) + fib(3k-5) = fib(3k-3) + 2*fib(3k-4) + fib(3k-5)
#                       = fib(3k-4) + fib(3k-5) + 2*fib(3k-4) + fib(3k-6) + fib(3k-7) = 3*fib(3k-4) + fib(3k-5) + fib(3k-6) + fib(3k-7)
#                       = 3*fib(3k-4) + fib(3k-4) + fib(3k-7) = 4*fib(3(k-1)-1) + fib(3(k-2)-1)
def solve2():
    a, b = 2, 8
    total = 0
    while a <= 4000000:
        total += a
        a, b = b, 4 * b + a
    return total

if __name__ == "__main__":
    result = solve()
    print(result)
    # Expected output: 4613732
    result2 = solve2()
    print(result2)
    # Expected output: 4613732
