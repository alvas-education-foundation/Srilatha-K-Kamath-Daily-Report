def string_length(string) :
    if string == '': 
        return 0
    else : 
        return 1 + string_length(string[1:])  
#main 
string=input('Enter string:')
print (string_length(string)) 
