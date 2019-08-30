def maxset(A):
    max_left = max_right = max_sum = -1
    temp_sum = left = 0
    for i, value in enumerate(A):
        #print (i, value)
        if value >= 0:
            temp_sum += value
            #print(temp_sum)
        else:
            if temp_sum > max_sum:
                max_sum = temp_sum
                max_left = left
                max_right = i
            #print(temp_sum, max_left, max_right)
            temp_sum = 0
            left = i+1
    else:
        if temp_sum > max_sum:
            #max_sum = temp_sum
            max_left = left
            max_right = len(A)
            #print(max_left)
    if max_left == max_right == -1:
        return []
    else:
        return (A[max_left:max_right])

A = [ 756898537, -1973594324, -2038664370, -184803526, 1424268980 ]
print(maxset(A))