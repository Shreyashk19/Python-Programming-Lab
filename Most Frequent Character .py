string = input("Enter a string: ")

frequency = {}

for char in string:
    if char != " ":
        frequency[char] = frequency.get(char, 0) + 1

most_frequent = max(frequency, key=frequency.get)

print("Most frequent character:", most_frequent)
print("Frequency:", frequency[most_frequent])