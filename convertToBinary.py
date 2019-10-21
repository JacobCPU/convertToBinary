def convertToBinary(num): #must take in a pos integer
    j =  0
    binString = ""  #binary string
    if num == 0:
        return "0"

    while num >= (2**(j)):
        j += 1 #to find number of digits

    for i in range(1, j+1):
        if (2**(j - i) <= num < 2**(j - i + 1)):
            binString += "1" #add 1 if in range
            num -= 2**(j - i)
        else:
            binString += "0"
    return binString
    
