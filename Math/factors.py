from math import sqrt

def allFactors(A):
    factors = []
    if A % 2 == 0:
        step = 1
    else:
        step = 2
    for i in range(1,A+1, step):
        if A % i == 0:
            factors.append(i)
                
    print(factors)

allFactors(9)