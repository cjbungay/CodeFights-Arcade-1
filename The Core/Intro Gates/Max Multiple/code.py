def maxMultiple(divisor, bound):
    res = bound % divisor
    return bound if res == 0 else bound - res