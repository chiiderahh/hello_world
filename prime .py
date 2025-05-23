import math

def is_prime(n):
    if n < 2:
        return false
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return false
    return true
