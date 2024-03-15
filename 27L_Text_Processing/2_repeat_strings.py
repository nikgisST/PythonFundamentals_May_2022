words = input().split(' ')
result = [word * len(word) for word in words]
print(''.join(result))



def repeat_func(word):
    return word * len(word)
# words = []
# words = input().split()
words: list = input().split(' ')
print(''.join(map(repeat_func, words)))




print(''.join(map(lambda word: word * len(word), input().split())))





def repeat_strings():
    filled_words = []
    for word in words:
        repeated_string = word * len(word)
        filled_words.append(repeated_string)
    print("".join(filled_words))


words = input().split()
repeat_strings()




words = input().split(' ')
result = ''
for word in words:
    result += word * len(word)
print(result)




class Example:
    def __init__(self, words):
        self.words = words

    def repeat_func(self):
        return ''.join(map(lambda x: x * len(x), self.words))


words: list = input().split()
obj = Example(words)
print(obj.repeat_func())


