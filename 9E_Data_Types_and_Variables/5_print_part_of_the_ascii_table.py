start_index = int(input())
final_index = int(input())
final_string = ""
for character in range(start_index, final_index + 1):
    final_string += chr(character) + " "                # + chr(32) === SPACE
print(final_string)




start_index = int(input())
final_index = int(input())
for character in range(start_index, final_index + 1):
    print(chr(character), end=" ")




# print(f"{final_string[0:-1]}")
# print{f"{final_string.strip()}")


start_index = int(input())
final_index = int(input())
final_string = ""
for character in range(start_index, final_index + 1):
    if character == final_string:
        final_string += chr(character)
    else:
        final_string += chr(character) + " "
print(final_string)


