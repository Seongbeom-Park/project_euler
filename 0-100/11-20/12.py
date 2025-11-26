# Problem 12: Highly Divisible Triangular Number

# Timeout
# def solve():
#     n = 0
#     d = 1
#     while True:
#         n += d
#         divider_count = 0
#         for i in range(1, int(n**1/2) + 1):
#             if n % i == 0:
#                 divider_count += 1
#         print(n, divider_count)
#         if divider_count > 500:
#             return n
#         d += 1

# n * (n+1) / 2
# the only common dividir of n and (n+1) is 1
# let #n be the number of divider of n
# #(n * (n+1) / 2) = #(n//2) * #(n+1) or #n * #((n+1)//2)
def get_divider_list(n):
    if n % 2 == 0:
        n = n // 2
    divider_list = []
    for i in range(1, int(n**1/2) + 1):
        if n % i == 0:
            divider_list += [i]
    divider_list += [n]
    return divider_list

def solve():
    n, n1 = 1, 2
    ln, ln1 = [1], [1]
    while len(ln) * len(ln1) < 500:
        n, n1 = n1, n1 + 1
        ln, ln1 = ln1, get_divider_list(n1)
    return n * n1 // 2

if __name__ == '__main__':
    print(solve())
    # Expected Output: 76576500
