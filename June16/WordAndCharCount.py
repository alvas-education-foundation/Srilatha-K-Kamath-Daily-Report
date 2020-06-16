string=input('Enter the String: ')
wordcount=0
charcount=0
for word in string.split():
  wordcount+=1
  for i in word:
    if(len(i)>0):
      charcount+=1
print('Word count is ',wordcount)
print('Character count is ',charcount)
