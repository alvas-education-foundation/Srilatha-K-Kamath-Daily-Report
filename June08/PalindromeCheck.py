def palindromecheck(string):
    if(string == string[:: - 1]):
        print("True")
    else:
        print("False")
#main
string = input("Enter the String : ")
palindromecheck(string)
