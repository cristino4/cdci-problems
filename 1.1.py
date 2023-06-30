testString = "cristino"

def check(word):
    b = len(testString)
    for i in range(0,len(testString)-1):
        b = b - 1
        for j in range(i+1,i+1+b):
            print('testing: ' + testString[i] + ' ' + testString[j])
            if testString[i] == testString[j]:
                print('found two equal letters at indexes: ' + str(i) + str(j))
                return 0
    print('did NOT find any equal letters')
    return 1
            
result = check(testString)
print(result)
