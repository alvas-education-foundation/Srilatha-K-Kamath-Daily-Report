str1=input('Enter string1:')
str2=input('Enter string2:')
c1=0
c2=0
for letter in str1:
    c1+=1
for letter in str2:
    c2+=1
if(c1>c2):
    print('The larger string is:',str1)
else:
    print("The larger string is:",str2)
