text = input()

emoticons = [text[ch + 1] for ch in range(len(text)) if text[ch] == ":"]

for el in emoticons:
    print(f":{el}")





def emoticon_finder(text):
    for index, colon in enumerate(text):
        if colon == ':':
            print(f'{colon}{text[index + 1]}')


string = input()
emoticon_finder(string)