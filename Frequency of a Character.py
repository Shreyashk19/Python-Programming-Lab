text = input("Enter a string: ")
char = input("Enter the character to find: ")
count = 0
for ch in text:
    if ch == char:
        count += 1
print("Frequency of", char, "is:", count)