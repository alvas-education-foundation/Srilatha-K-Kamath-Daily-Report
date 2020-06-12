s=input("Enter string:")
count = 0
vowels = set("aeiouAEIOU")
for letter in s:
    if letter in vowels:
        count += 1
print("Count of the vowels is:")
print(count)
