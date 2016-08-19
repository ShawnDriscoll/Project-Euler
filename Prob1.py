
def multiples(a, b, n):
    naturals = []
    for i in xrange(1, n):
        if i % a == 0 or i % b == 0:
            naturals.append(i)
    return naturals


if __name__ == '__main__':
    a = 3
    b = 5
    n = 1000
    the_naturals = multiples(a, b, n)
    print the_naturals
    print
    print sum(the_naturals)
    