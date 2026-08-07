str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if sorted(str1.replace(" ", "").lower()) == sorted(str2.replace(" ", "").lower()):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")