# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/

def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}

    # The running integer that's checked for primeness
    q = 2

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1


def is_prime(n):
    '''Check whether n is a prime number'''
    '''
    >>> is_prime(2)
    True

    >>> is_prime(3)
    True

    >>> is_prime(10)
    False

    '''
    if n<=1:
       return False
    for i in range(2,int(n**0.5+1)):
        if n%i==0:
            return False
    return True


def factorial(n):
    '''Calculate factorial of n, n!'''
    '''
    >>> factorial(0)
    1

    >>> factorial(1)
    1

    >>> factorial(2)
    2

    >>> factorial(3)
    6

    >>> factorial(5)
    120
    '''
    if n==0 or n==1:
        return 1
    p = 1
    for i in range(2,n+1):
        p *= i
    return p

def coins(s,n,recursive=False):
    '''Dynamic programming for coins summation
    s, list of possible coins
    n, the summation
    Returns the number of different ways that n can be made using any number of elements in s
    Recursion is possible, but takes more time for large numbers
    '''
    '''
    >>> coins([1,2],4)
    3

    >>> coins([1,2,3,4],5)
    6

    >>> coins([1,2,5,10,20,50,100,200],200, recursive=True)
    73682
    
    >>> coins([1,2,5,10,20,50,100,200],200)
    73682
    
    >>> coins([3,5],7)
    0
    
    >>> coins(list(range(1,100)),100)
    190569291
    '''
    if not recursive:
        c = [1] + [0]*n
        for i in s:
            for j in range(i,n+1):
                c[j] += c[j-i]
        return c[-1]
    else:
        if n == 0:
            return 1
        if n < 0:
            return 0
        if s == []:
            return 0
        return coins(s[:-1],n,recursive=False) + coins(s,n-s[-1],recursive=False)



def _test():
    import doctest, ekailia
    doctest.testmod(ekailia)


if __name__ == '__main__':
    _test()    