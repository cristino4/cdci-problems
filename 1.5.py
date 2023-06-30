
str1 = 'hello'
str2 = 'hells'
str3 = 'mustv'
str4 = 'hellws'


def checkLengths(string1,string2):
    check = abs(len(string1)-len(string2))
    print('length diff check: ' + str(check))
    return check
    
def checkCharDiffSameLength(string1, string2):
    counter = 0
    for i in range(0, len(string1)):
        if string1[i] != string2[i]:
            counter += 1
    print('charDiff counter: ' + str(counter))
    return counter


    
def check(string1, string2):
    charDiff = checkCharDiffSameLength(string1,string2)

    lengthCheck = checkLengths(string1,string2)

    if lengthCheck == 0:
        if charDiff > 1:
            print('strings differ by ' + str(charDiff) + ' edits')
            return False
        elif charDiff == 0:
            print('strings are exactly the same')
            return True
        elif charDiff == 1:
            print('strings are 1 edit away')
            return True
    elif lengthCheck > 1:
        print('strings differ by ' +str(lengthCheck) + ' edits')
        return False
    elif lengthCheck == 1:
        index1 = 0
        index2 = 0
        while index1 < len(string1) and index2 < len(string2):
            if string1[index1] != string2[index2]:
                if index1 != index2:
                    print('strings differ by more than 1 edit')
                    return False
                index2 += 1
            else:
                index1 += 1
                index2 += 1
            print('strings differ by 1 edit')
            return True


check(str4,str2)