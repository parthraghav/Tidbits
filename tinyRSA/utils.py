# Utility functions

from random import randrange, getrandbits, choice
from math import gcd
import string

def is_prime_deterministic(n):
	if not n % 2:
		return  False

	for i in range(3, sqrt(n), 2):
		if not n % i:
			return False

	return True

def get_coprimes(n, t):
	Coprimes = []
	for i in range(1, t):
		if gcd(i, n) == 1:
			Coprimes.append(i)
	return Coprimes

def find_coprime(n, t):
	for i in range(n//2, t):
		if gcd(i, n) == 1:
			return i

def rand_str(L=6, alphabet=string.ascii_uppercase + string.digits):
	return ''.join(choice(alphabet) for x in range(L))

def mod_inv(a, b):
	g, x, y = gcdExt(a, b)
	if g != 1:
		return ValueError("Inverse doesn't exist")
	else:
		res = (x%b + b)%b
		return res

def gcdExt(a, b):
	if a == 0:
		return (b, 0, 1)
	gcd_res, xo, yo = gcdExt(b%a, a)
	x = yo - (b//a)*xo
	y = xo
	return (gcd_res, x, y)

# Implementation borrowed from this blog post
# https://medium.com/@prudywsh/how-to-generate-big-prime-numbers-miller-rabin-49e6e6af32fb
def is_prime(n, k=128):
    """ Test if a number is prime
        Args:
            n -- int -- the number to test
            k -- int -- the number of tests to do
        return True if n is prime
    """
    # Test if n is not even.
    # But care, 2 is prime !
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    # find r and s
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    # do k tests
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True

def generate_prime_candidate(length):
    """ Generate an odd integer randomly
        Args:
            length -- int -- the length of the number to generate, in bits
        return a integer
    """
    # generate random bits
    p = getrandbits(length)
    # apply a mask to set MSB and LSB to 1
    p |= (1 << length - 1) | 1
    return p

def generate_prime_number(length=1024):
    """ Generate a prime
        Args:
            length -- int -- length of the prime to generate, in          bits
        return a prime
    """
    p = 4
    # keep generating while the primality test fail
    while not is_prime(p, 128):
        p = generate_prime_candidate(length)
    return p


