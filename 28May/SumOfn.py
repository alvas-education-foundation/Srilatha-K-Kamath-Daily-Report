Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. This is only applicable to the natural numbers.
def digital_root(num):
    if(num<10):
        return num
    else:
        return digital_root((num%10)+digital_root(num//10))1
num=int(input('Enter the num '))
print(digital_root(num))

