def checkPalindrome(inputString):
    revString = ''
    l=len(inputString)
    for i in range(l):
        revString+=inputString[(l-1)-i]
    if (revString == inputString):
        return True
    else:
        return False
        