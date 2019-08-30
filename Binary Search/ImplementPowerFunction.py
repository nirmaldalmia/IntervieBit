def pow(x,n,d):
    if x == 0:
        return 0
    if n == 0:
        return 1
    return ((x**n)%d)

x = 2
n = 3
d =  3
print(pow(x,n,d))