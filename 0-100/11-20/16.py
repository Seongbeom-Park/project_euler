# Problem 16: Power Digit Sum

def solve(n, m):
    return sum([int(i) for i in str(n**m)])

# # 0, 1, 2, 3,    4,    5, 6, 7,    8,    9,10,...
# # 1, 2, 4, 8, (1)6, (1)2, 4, 8, (1)6, (1)2, 4,...
# def solve_2(n, m):
#     if n != 2:
#         return -1
#     quotient, remainder = n // 4, n % 4
#     return 2**remainder + solve_2(n, )

# # TODO

if __name__ == '__main__':
    print(solve(2, 1000))
    # Expected Output: 1366
    # print(solve_2(2, 1000))
