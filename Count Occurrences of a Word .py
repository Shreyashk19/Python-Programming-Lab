sentence = input("Enter a sentence: ")
word = input("Enter the word to count: ")

words = sentence.split()

count = words.count(word)

print("The word appears", count, "times")