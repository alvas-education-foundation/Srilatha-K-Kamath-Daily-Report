def palindromechk(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return palindromechk(s[1:-1])
        else:
            return False
string=input("Enter string:")
if(palindromechk(string)==True):
    print("String is a palindrome!")
else:
    print("String isn't a palindrome!")
