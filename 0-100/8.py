# Problem 8: Largest Product in a Series

STRING = '''
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
'''
STRING = STRING.replace('\n', '')

# iterate 13-size window
def solve():
    numbers = []
    for i in range(13):
        n = int(STRING[i])
        numbers += [n]
    def calc_mul():
        mul = 1
        for n in numbers:
            mul *= n
        return mul
    max_mul = calc_mul()
    for s in STRING:
        if s == '\n':
            continue
        n = int(s)
        numbers.pop(0)
        numbers += [n]
        max_mul = max(max_mul, calc_mul())
    return max_mul

# prefix sum
def solver(string):
    numbers = []
    mul = 1
    for i in range(13):
        n = int(string[i])
        numbers += [n]
        mul *= n
    def calc_mul():
        mul = 1
        for n in numbers:
            mul *= n
        return mul
    max_mul = calc_mul()
    for s in string:
        n = int(s)
        left = numbers.pop(0)
        numbers += [n]
        if left != 0:
            mul /= left
            mul *= n
        else:
            mul = calc_mul()
        max_mul = max(max_mul, calc_mul())
    return max_mul
def solve_2():
    return solver(STRING)

# split string by 0
def solve_3():
    strings = STRING.split('0')
    strings = list(filter(lambda x: len(x) >= 13, strings))
    max_mul = 0
    for string in strings:
        max_mul = max(max_mul, solver(string))
    return max_mul

if __name__ == '__main__':
    print(solve())
    # Expected Output: 23514624000
    print(solve_2())
    print(solve_3())
