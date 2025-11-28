# Problem 6: Sum Square Differene

# iterate numbers and calculate sum and sum of square
def solve():
    sum_of_squares = 0
    sum_of_numbers = 0
    for i in range(1, 101):
        sum_of_squares += i**2
        sum_of_numbers += i
    return sum_of_numbers**2 - sum_of_squares

# sum_of_numbers = n * (n+1) / 2
# sum(1, n) = O(n^2)
# sum(1, n^2) = O(n^3)?
# f(n) = a*n^3 + b*n^2 + c*n + d
# f(0) = 0 = d
# f(1) = 1 = a + b + c + d
# f(2) = 5 = 8a + 4b + 2c + d
# f(3) = 14 = 27a + 9b + 3c + d
# a = 1/3, b = 1/2, c = 1/6, d = 0
# f(n) = 1/6*(2*n^3 + 3*n^2 + n)

# f(1) = 1 = 1/6*(2 + 3 + 1)
# f(k+1) = 1/6*(2*(k+1)^3 + 3*(k+1)^2 + (k+1))
#        = 1/6*(2*k^3 + 6*k^2 + 6*k + 2 + 3*k^2 + 6*k + 3 + k + 1)
#        = 1/6*(2*k^3 + 3*k^2 + k + 6*k^2 + 12*k + 6) = f(k) + (k+1)^2
def solve_2():
    n = 100
    square_of_sum = (n * (n + 1) // 2)**2
    sum_of_square = (2*n**3 + 3*n**2 + n) // 6
    return square_of_sum - sum_of_square

if __name__ == '__main__':
    print(solve())
    # Expected Output: 25164150
    print(solve_2())
