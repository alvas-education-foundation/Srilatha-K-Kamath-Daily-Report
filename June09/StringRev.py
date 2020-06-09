def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]
#main
string=input('Enter string to be reversed:')
print('Reversed string is:',reverse(string))
