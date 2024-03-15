number = int(input())
synonyms = {}

for _ in range(number):
    word, synonym = input(), input()
    if word in synonyms:
        synonyms[word].append(synonym)
    elif word not in synonyms:
        synonyms[word] = [synonym]

data = [f"{word} - {', '.join(synonym)}" for word, synonym in synonyms.items()]
print('\n'.join(data))




from collections import defaultdict

number = int(input())
synonyms = defaultdict(list)

for _ in range(number):
    word, synonym = input(), input()
    synonyms[word].append(synonym)

data = [f"{word} - {', '.join(synonym)}" for word, synonym in synonyms.items()]
print('\n'.join(data))





number = int(input())
synonyms = {}
for i in range(number):
    word = input()
    synonym = input()
    if word in synonyms:
        synonyms[word].append(synonym)
    elif word not in synonyms:
        synonyms[word] = []
        synonyms[word].append(synonym)
for word in synonyms:
    print(f"{word} - {', '.join(synonyms[word])}")




number = int(input())
synonyms = {}

for i in range(number):
    word = input()
    synonym = input()
    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(synonym)

for word in synonyms:
    print(f"{word} - {', '.join(synonyms[word])}")