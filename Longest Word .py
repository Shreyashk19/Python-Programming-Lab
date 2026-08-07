sentence = input("Enter a sentence: ")
longest = ""
word = ""
for ch in sentence + " ":
    if ch != " ":
        word += ch
    else:
        if len(word) > len(longest):
            longest = word
        word = ""
print("Longest word is:", longest)