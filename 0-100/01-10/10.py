# Problem 10: Summation of Primes

# find all primes below two million
# Timeout
# def solve(n):
#     primes = []
#     for i in range(2, n):
#         is_prime = True
#         for p in primes:
#             if i % p == 0:
#                 is_prime = False
#         if is_prime:
#             primes += [i]
#     return sum(primes)

# search only odd number
# Timeout
# def solve(n):
#     primes = [2]
#     for i in range(3, n, 2):
#         is_prime = True
#         for p in primes:
#             if i % p == 0:
#                 is_prime = False
#         if is_prime:
#             primes += [i]
#     return sum(primes)

# search 6k +1 +5
# Timeout
def solve(n):
    primes = [2, 3, 5]
    for i in range(6, n, 6):
        j = i + 1
        is_prime = True
        for p in primes:
            if j % p == 0:
                is_prime = False
        if is_prime:
            primes += [j]
        j = i + 5
        is_prime = True
        for p in primes:
            if j % p == 0:
                is_prime = False
        if is_prime:
            primes += [j]
    return sum(primes)

# 30k + 1   
# 30k + 3   x
# 30k + 5   x
# 30k + 7   
# 30k + 9   x
# 30k + 11  
# 30k + 13  
# 30k + 15  x
# 30k + 17  
# 30k + 19  
# 30k + 21  x
# 30k + 23  
# 30k + 25  x
# 30k + 27  x
# 30k + 29  
# search 30k + [1,7,11,13,17,19,23,29]
# Timeout
# def solve(n):
#     primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
#     offsets = [1, 7, 11, 13, 17, 19, 23, 29]
#     for i in range(30, n, 30):
#         for offset in offsets:
#             j = i + offset
#             if j >= n:
#                 break
#             is_prime = True
#             for p in primes:
#                 if j % p == 0:
#                     is_prime = False
#             if is_prime:
#                 primes += [j]
#     print(primes)
#     return sum(primes)

# enlarge window automatically
# [2] 2k + [1]
# [2,3] 6k + [1,5]
# [2,3,5] 30k + [1,7,11,13,17,19,23,29]
# Timeout
# def solve(n):
#     primes = [2]
#     window_end_index = 0
#     window = 1
#     while primes[-1] < n:
#         window *= primes[window_end_index]
#         offsets = []
#         for offset in range(1, window):
#             is_relative_prime = True
#             for p in primes[0:window_end_index + 1]:
#                 if offset % p == 0:
#                     is_relative_prime = False
#                     break
#             if is_relative_prime:
#                 offsets += [offset]
#         # print(primes[0:window_end_index + 1], window, offsets)
#         for i in range(window, 2 * window, window):
#             for offset in offsets:
#                 j = i + offset
#                 if j >= n:
#                     break
#                 is_prime = True
#                 for p in primes:
#                     if j % p == 0:
#                         is_prime = False
#                 if is_prime:
#                     primes += [j]
#         for i in range(2 * window, window * primes[window_end_index + 1], window):
#             if i >= n:
#                 break
#             for offset in offsets:
#                 j = i + offset
#                 is_prime = True
#                 for p in primes:
#                     if j % p == 0:
#                         is_prime = False
#                 if is_prime:
#                     primes += [j]
#         window_end_index += 1
#     sum_of_primes = 0
#     for p in primes:
#         if p >= n:
#             break
#         sum_of_primes += p
#     print(list(filter(lambda x: x <= n, primes)))
#     return sum_of_primes

# marking based prime number finding algorithm
def solve(n):
    mask = [0] * n
    sum_of_primes = 0
    for i in range(2, n):
        if mask[i] == 0:
            sum_of_primes += i
            j = i + i
            while j < n:
                mask[j] = 1
                j += i
    return sum_of_primes

# search odd-number only
def solve_2(n):
    mask = [0] * n
    sum_of_primes = 2
    for i in range(3, n, 2):
        if mask[i] == 0:
            sum_of_primes += i
            j = i + i
            while j < n:
                mask[j] = 1
                j += i
    return sum_of_primes

# search 6k + [1,5] only
def solve_3(n):
    mask = [0] * n
    sum_of_primes = 2 + 3 + 5
    offsets = [1, 5]
    for i in range(6, n, 6):
        for offset in offsets:
            k = i + offset
            if k < n and mask[k] == 0:
                sum_of_primes += k
                j = k + k
                while j < n:
                    mask[j] = 1
                    j += k
    return sum_of_primes

if __name__ == '__main__':
    print(solve(2000000))
    # Expected Ouptput: 142913828922
    print(solve_2(2000000))
    print(solve_3(2000000))
