#tests whether myString is a palindrome
def isPalindrome(myString):
    tempString = myString
    length = len(tempString)
    half = length/2
    isPalindrome = True
    for i in range(0, int(half)):
        if myString[i] != tempString[(length-1)-i]:
            isPalindrome = False
    print(isPalindrome)

#no errors below this line
def main():
    print("Should print: True\nPrints: ",end="")
    isPalindrome("oozyratinasanitaryzoo")
    print("Should print: False\nPrints:", end="")
    isPalindrome("18101181")
main()
