messages = input().split()
final_message = []
for every_piece_message in messages:
    number = ""
    current_message = ""
    for character in every_piece_message:
        if character.isdigit():
            number += character
        else:
            break
    every_piece_message = every_piece_message.replace(number, "")
    number = int(number)
    current_message += chr(number)
    if len(every_piece_message) >= 2:
        every_piece_message = every_piece_message[-1] + every_piece_message[1:-1] + every_piece_message[0]
    current_message += every_piece_message
    final_message.append(current_message)
print(" ".join(final_message))


messages = input().split()
final_message = []
for every_piece_message in messages:
    characters = [char for char in every_piece_message if not char.isdigit()]
    nums = [char for char in every_piece_message if char.isdigit()]
    ascii_char = [chr(int("".join(nums)))]
    current_word = ascii_char + characters
    current_word[1], current_word[-1] = current_word[-1], current_word[1]
    final_message.append("".join(current_word))
print(" ".join(final_message))



some_string = "Gosho"                                                     # това става само когато работим с листове LISTS
some_string[0], some_string[-1] = some_string[-1], some_string[0]
print(some_string)                                                        #STR OBJECT DOES NOT SUPPORT ITEM ASSIGNMENT



def get_digits(some_string):
    number = ""
    for character in some_string:
        if character.isdigit():
            number += character
        else:
            break
    return number


messages = input().split()
final_message = []
for message in messages:
    current_message = ""
    number = int(get_digits(message))
    message = message.replace(str(number), "")
    current_message += chr(number)
    if len(message) >= 2:
        message = message[-1] + message[1:-1] + message[0]
    current_message += message
    final_message.append(current_message)
print(" ".join(final_message))













