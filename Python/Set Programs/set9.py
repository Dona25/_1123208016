sentence = input("Enter a sentence: ")
words = sentence.split()
unique = set(words)
print("Unique words =", len(unique))