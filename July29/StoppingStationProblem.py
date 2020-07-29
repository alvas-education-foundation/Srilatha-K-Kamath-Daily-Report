def stopping_station( p, n):
    num = 1
    dem = 1
    s = p
    while p != 1:
        dem *= p
        p-=1
    t = n - s + 1
    while t != (n-2 * s + 1):
        num *= t
        t-=1
    if (n - s + 1) >= s:
        return int(num/dem)
    else:
        return -1
num = stopping_station(4, 12)
if num != -1:
    print(num)
else:
    print("Not Possible") 
