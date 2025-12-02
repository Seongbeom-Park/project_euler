# Problem 15: Lattice Paths

# need to go right n times, go down m times: n+m comb n
def solve(n, m):
    import math
    return math.comb(n+m, n)

# solution: recursive
# Timeout
# def solve_2(i, j):
#     if i == 0 and j == 0:
#         return 1
#     if i < 0 or j < 0:
#         return 0
#     return solve_2(i-1, j) + solve_2(i, j-1)

# solution: recursive and memo
memo = { (0, 0): 1 }
def solve_2(i, j):
    if (i, j) in memo:
        return memo[(i, j)]
    if i < 0 or j < 0:
        return 0
    memo[(i, j)] = solve_2(i-1, j) + solve_2(i, j-1)
    return memo[(i, j)]

# solution: iterative
def solve_3(n, m):
    grid = {(i, j): 0 for i in range(n+1) for j in range(m+1)}
    grid[(0, 0)] = 1
    for i in range(n+1):
        grid[(i, 0)] = 1
    for j in range(m+1):
        grid[(0, j)] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            grid[(i, j)] = grid[(i-1, j)] + grid[(i, j-1)]
    return grid[(n, m)]

if __name__ == '__main__':
    print(solve(20, 20))
    # Expected Output: 137846528820
    print(solve_2(20, 20))
    print(solve_3(20, 20))
