def float_octal(number, places = 3):
    whole, dec = str(number).split(".")  
    whole = int(whole)
    dec = int (dec)
    res = oct(whole).lstrip("0o") + "."
    for x in range(places):  
        whole, dec = str((decimal_converter(dec)) * 8).split(".")
        dec = int(dec)  
        res += whole
    return res
def decimal_converter(num):
    while num > 1:
        num /= 10
    return num
#main
n = input("Enter your floating point value : \n")
p = int(input("Enter the number of decimal places of the result : \n"))
print(float_octal(n, places = p)) 
