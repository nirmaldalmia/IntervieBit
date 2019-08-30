def primesum(A):
    def isPrime(n):
        if n < 2:
            return False
        for i in range(2,n//2+1):
            if n%i == 0:
                return False
        return True
            
    for i in range(2,A):
        if isPrime(i) and isPrime(A-i):
            #if i + A - i == A:
            return [i, A-i]

print(primesum(16777214))