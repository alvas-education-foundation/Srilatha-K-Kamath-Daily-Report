def odd_values_string(str):
  result = "" 
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  print('The resultant string:',result)
#main
string=input('Enter the string:')
odd_values_string(string)
  
