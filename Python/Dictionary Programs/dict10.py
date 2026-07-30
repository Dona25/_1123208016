sentence = input("Enter a sentence: ")
words = sentence.split()
d = {}
for word in words:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
most = max(d, key=d.get)
print("Most Frequent Word:", most)