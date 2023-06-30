str1 = 'aabccccaaa'
freqTable = {}
newString = ''
def check(string1):    


    for i in range(0, len(string1)):
        print('i: '+ str(i))
        if string1[i] not in freqTable:
            freqTable[string1[i]] = 0
        freqTable[string1[i]] += 1
        if string1[i] != string1[i-1]:
            newString.
    print(freqTable)





check(str1)
