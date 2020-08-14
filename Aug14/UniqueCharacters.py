def isUniqueChars(st):
    if len(st) > 256:
        return False
    char_set = [False] * 128
    for i in range(0, len(st)):
        val = ord(st[i])
        if char_set[val]:
            return False
        char_set[val] = True
    return True
#main
st = input('Enter the string:')
print(isUniqueChars(st)) 
