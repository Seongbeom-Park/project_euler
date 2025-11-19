# Problem Zero
# iterate from 1 to 608 thousand and add if the number is odd square
def solve():
    total = 0
    for i in range(1, 608001):
        if i % 2 == 1:  # Check if the number is odd
            total += i * i  # Add the square of the number
    return total

if __name__ == "__main__":
    result = solve()
    print(result)
    # Expected output: 37459285333232000
