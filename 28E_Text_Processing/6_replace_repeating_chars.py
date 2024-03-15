text = input()
text_list = []

for letter in range(0, len(text) - 1):
    if not text[letter] == text[letter + 1]:
        text_list.append(text[letter])

text_list.append(text[-1])

print(f"{''.join(text_list)}")






text = input()
new_text = text[0]

for i in range(1, len(text)):
    if not text[i - 1] == text[i]:
        new_text += text[i]

print(new_text)





# def replace_repeating_characters(string):
#     for index, char in enumerate(string):
#         try:
#             if string[index + 1] != char:
#                 print(char, end='')
#         except IndexError:
#             print(char, end='')
#
#
# string = input()
# replace_repeating_characters(string)

