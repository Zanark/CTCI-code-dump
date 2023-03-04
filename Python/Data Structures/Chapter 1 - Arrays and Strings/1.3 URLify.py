def URLify(inputString, trueLength):
    if len(inputString) > trueLength:
        inputString = inputString[0:trueLength]
    urlString = ''
    for c in inputString:
        if c == ' ':
            c = '%20'
        urlString += c 
    return urlString    

if __name__ == '__main__':
    inputString = input("Enter the string >> \t")
    trueLength = int(input("Enter the true length of the string >> \t"))
    print("URL-ified string >> " + str(URLify(inputString, trueLength)))