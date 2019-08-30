def convertToTitle(A):
    string = ""
    while A > 0:
        diff = (A-1)%26
        character = chr(diff + ord('A'))
        string += character
        A = (A-1)//26
    return string[::-1]

print(convertToTitle(943566))