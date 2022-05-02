# This program is searching for nine digit sequence in text then checkig whether
# it is a valid Israeli ID

# This function is getting an int number and summing all its digits up to singal
# number
def multiDigitsToOne(num):
    sum = 0
    temp = int(num)
    for i in range(len(str(num))):
        sum += temp%10
        temp /= 10
        temp = int(temp)

    if int(sum/10) != 0:
        sum = multiDigitsToOne(sum)
        
    return sum

# This function validate that a number is a valid Israeli ID      
def israeliIdCheck(num):
    IL_ID_LEN = 9
    valid = False
    temp = list(map(int,str(num)))
    if len(str(num)) == IL_ID_LEN:
        for i in range(IL_ID_LEN-1):
            if i%2 != 0:
                temp[i] = multiDigitsToOne(temp[i]*2)
        valid = (sum(temp)%10 == 0)
                                   
    return valid
