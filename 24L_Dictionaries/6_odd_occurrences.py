from collections import defaultdict

words = input().split(' ')
dictionary = defaultdict(int)
for word in words:
    dictionary[word.lower()] += 1
print(' '.join([word for word, count in dictionary.items() if count % 2 != 0]))





words = input().split(" ")
dictionary = {}
for word in words:
    word_lower = word.lower()
    if word_lower not in dictionary:
        dictionary[word_lower] = 0
    dictionary[word_lower] += 1
for (key, value) in dictionary.items():
    if value % 2 != 0:
        print(key, end=" ")