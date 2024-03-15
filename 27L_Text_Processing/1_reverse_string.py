def reverse_func(data):
    for string in data:
        print(f'{string} = {string[::-1]}')


words = []
while True:
    word = input()
    if word == 'end':
        break
    words.append(word)

reverse_func(words)




words = []
while True:
    word = input()
    if word == 'end':
        break
    words.append(word)
    print(f'{word} = {word[::-1]}')




word = input()
while word != "end":
    text_reversed = ""
    for ch in reversed(word):
        text_reversed += ch
    print(word + " = " + text_reversed)
    word = input()