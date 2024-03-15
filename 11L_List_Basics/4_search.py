number = int(input())
given_word = input()

list = []

for _ in range(number):
    current_sentence = input()
    list.append(current_sentence)
print(list)

for iteration in range(len(list)-1, -1, -1): #iterating through the strings reversed (so we don't skip elements when removing)
    sentence = list[iteration]
    if given_word not in sentence:
        list.remove(sentence)
print(list)

