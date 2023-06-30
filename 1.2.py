str1 =  'hello'
str2 = 'lleeh'

#check if both strings are a permutation of eachother
def check(string1, string2):
    #check if the strings are the same length
    if len(str1) != len(str2):
        return 0
    
    freqArr = [0] * 128
    ascii_chars = []

    for char in str1:
        freqArr[ord(char)] += 1
    print(freqArr)
    
    for char in str2:
        freqArr[ord(char)] -= 1
        if freqArr[ord(char)] < 0:
            return 0
    print(freqArr)
    return 1

result = check(str1,str2)
print(result)