# You’re given a read only array of n integers. Find out if any integer occurs more than n/3 times in the array in linear time and constant additional space.

# If so, return the integer. If not, return -1.

# If there are multiple solutions, return any one.

# Example :

# Input : [1 2 3 1 1]
# Output : 1 
# 1 occurs 3 times which is more than 5/3 times. 

#####################################################################################################################################################################

def repeatedNumber(A):
    hashmap = {}
    A = list(A)
    n = len(A)
    for number in A:
        if number in hashmap:
            hashmap[number] += 1
        else:
            hashmap[number] = 1
    
    for key,value in hashmap.items():
        if value > n/3:
            return key
    return -1

A = [1, 2, 3, 1, 1]
print(repeatedNumber(A))