def check():

    str1 = '   Mr John Smith in Germany '
    strStripped = str1.strip()
    length = 13
    print('initial string: ' + str1)
    print('stripped string: ' + strStripped)
    replaceChar = '%20'
    counter = 0
    newstr1 = ''
    for char in strStripped:
        print('counter: ' + str(counter))
        if char == ' ':
            newstr1 = strStripped.replace(' ', '%20')
            counter += 1
            print('string with %20: ' + newstr1)

check()    
