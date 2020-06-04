string=input("Enter the string:")
#print(string)
lst=string.split('-')
lst.sort()
delim='-'
s=delim.join(lst)
print("The string after sorting is:",s)
