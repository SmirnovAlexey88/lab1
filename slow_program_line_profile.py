from decimal import *
from line_profiler import profile

@profile
def exp(x):
    getcontext().prec += 2
    i, lasts, s, fact, num = 0, 0, 1, 1, 1
    while s != lasts:
        lasts = s
        i += 1
        fact *= i
        num *= x
        s += num / fact
    getcontext().prec -= 2
    return +s

exp(Decimal(150))
exp(Decimal(400))
exp(Decimal(3000))
