def permutatedStrings(inputString1, inputString2):
    if len(inputString1) != len(inputString2):
        return False
    combinedCharSet = {}
    for c in inputString1:
        if c in combinedCharSet:
            combinedCharSet[c] += 1
        else:
            combinedCharSet[c] = 1
    for c in inputString2:
        if (c in combinedCharSet):
            combinedCharSet[c] -= 1
    for freq in combinedCharSet.values():
        if freq == 0:
            continue
        else:
            return False
    return True
    

if __name__ == '__main__':
    inputString1 = input("Enter string1 >> \t")
    inputString2 = input("\nEnter string2 >> \t")
    print("Are the two strings permutations of each other? >>\t" + str(permutatedStrings(inputString1, inputString2)))