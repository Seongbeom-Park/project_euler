# Problem 9: Special Pythagorean Triplet

# iterate 3 numbers which sum of them is equal to 1000
def solve():
    n = 1000
    for a in range(1, 1000):
        for b in range(a + 1, 1000):
            c = 1000 - (a + b)
            if c < a:
                break
            if a**2 + b**2 == c**2:
                return a*b*c

if __name__ == '__main__':
    print(solve())
    # Expected Output: 31875000
