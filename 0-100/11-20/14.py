# Problem 14: Longest Collatz Sequence

# 1. iterate and count chain length
# RecursionError: maximum recursion depth exceeded
# def get_collatz_length(n, l = 0):
#     if n == 1:
#         return l + 1
#     if n % 2 == 0:
#         return get_collatz_length(n//2, l + 1)
#     else:
#         return get_collatz_length(3*n + 1, l + 1)

# def solve():
#     max_length = 0
#     for i in range(1000000):
#         length = get_collatz_length(i)
#         max_length = max(length, max_length)
#     return max_length

# Timeout
# def get_collatz_length(n):
#     length = 1
#     while n != 1:
#         if n % 2 == 0:
#             n = n // 2
#         else:
#             n = 3*n + 1
#         length += 1
#     return length

# def solve():
#     max_length = 0
#     for i in range(1000000):
#         length = get_collatz_length(i)
#         max_length = max(length, max_length)
#     return max_length

# 2. memoize
def solve():
    memo = { 1: 1 }
    for n in range(1, 1000001):
        if n in memo:
            continue
        sequence = [n]
        while True:
            if n % 2 == 0:
                n = n//2
            else:
                n = 3*n + 1
            sequence += [n]
            if n in memo:
                break
        length = memo[sequence[-1]]
        for n in reversed(sequence[:-1]):
            length += 1
            memo[n] = length
    max_n, max_len = 0, 0
    for n in range(1, 1000001):
        length = memo[n]
        if max_len < length:
            max_n = n
            max_len = length
    return max_n

if __name__ == '__main__':
    print(solve())
    # Expected Output: 837799
