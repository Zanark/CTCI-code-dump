def isUnique(inputString):
    if len(inputString) > 128:
        return False
    charSet = set()
    for c in inputString:
        if c in charSet:
            return False
        else:
            charSet.add(c)
    return True    

if __name__ == '__main__':
    inputString = input("Enter the string >> \t")
    print("Does the string have Unique characters >> " + str(isUnique(inputString)))