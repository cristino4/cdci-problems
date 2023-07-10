testString = 'erbottlewat'+'erbottlewat'
testSubstring = 't'





def isSubstring(string, substring):
    print('string: '+string)
    print('substring: ' +substring)
    for i in range(0,len(string)-len(substring)):
        print('i: '+str(i))
        print('if '+substring+ ' equals '+string[i:len(substring)+i])
        if substring == string[i:len(substring)+i]:
            print(substring+ ' is a substring!')
            return True
    print(substring + ' is NOT a substring')
    return False

isSubstring(testString,testSubstring)