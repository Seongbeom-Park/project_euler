# Problem 4: Largest Palindrome Product

# iterate two 3-digit numbers
def is_palindrome(n):
    s = str(n)
    if len(s) == 6:
        return (s[0] == s[5]) and (s[1] == s[4]) and (s[2] == s[3])
    if len(s) == 5:
        return (s[0] == s[4]) and (s[1] == s[3])
    return False

def solve():
    max_palindrome = 0
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            n = i * j
            if n < max_palindrome:
                continue
            if is_palindrome(n):
                max_palindrome = max(max_palindrome, n)
    return max_palindrome

# iterate all 3-digit pairs
def solve_1():
    max_palindrome = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            n = i * j
            if is_palindrome(n) and n > max_palindrome:
                max_palindrome = n
    return max_palindrome

# iterate 3-digit pairs except common set
def solve_2():
    max_palindrome = 0
    for i in range(100, 1000):
        for j in range(i, 1000):
            n = i * j
            if is_palindrome(n) and n > max_palindrome:
                max_palindrome = n
    return max_palindrome

# 3rd solution iterate reversely
def solve_3():
    max_palindrome = 0
    for i in range(999, 99, -1):
        for j in range(999, i-1, -1):
            n = i * j
            if n < max_palindrome:
                continue
            if is_palindrome(n):
                max_palindrome = max(max_palindrome, n)
    return max_palindrome

# 4th solution
# 6-digit palindrome = 100000x + 10000y + 1000z + 100z + 10y + x
#                    = 100001x + 10010y + 1100z
#                    = 11(9091x + 910y + 100z)
# i or j should be multiple of 11
def solve_4():
    max_palindrome = 0
    for i in range(999, 99, -1):
        if i % 11:
            j_start = 990
            dj = -11
        else:
            j_start = 999
            dj = -1
        for j in range(j_start, i-1, dj):
            n = i * j
            if n < max_palindrome:
                continue
            if is_palindrome(n):
                max_palindrome = max(max_palindrome, n)
    return max_palindrome

# NOTE: fix j to be multiple of 11 (simple but slow)
def solve_5():
    max_palindrome = 0
    for i in range(999, 99, -1):
        for j in range(990, 99, -11):
            n = i * j
            if n < max_palindrome:
                continue
            if is_palindrome(n):
                max_palindrome = max(max_palindrome, n)
    return max_palindrome

# NOTE: memoize calculated numbers
def solve_6():
    max_palindrome = 0
    memo = set([])
    for i in range(999, 99, -1):
        for j in range(990, 99, -11):
            n = i * j
            if n in memo:
                continue
            memo.add(n)
            if n < max_palindrome:
                continue
            if is_palindrome(n):
                max_palindrome = max(max_palindrome, n)
    return max_palindrome

if __name__ == '__main__':
    result = solve()
    print(result)
    # Expected output: 906609
    resule_1 = solve_1()
    print(resule_1)
    resule_2 = solve_2()
    print(resule_2)
    resule_3 = solve_3()
    print(resule_3)
    resule_4 = solve_4()
    print(resule_4)
    resule_5 = solve_5()
    print(resule_5)
    resule_6 = solve_6()
    print(resule_6)
