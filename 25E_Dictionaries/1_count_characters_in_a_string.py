letters = {}
symbols = "".join(s for s in input().split())
for letter in symbols:
    # if letter not in letters:
    # #     letters[letter] = 1
    # # elif letter in letters.keys():
    # #     letters[letter] += 1

    if letter not in letters.keys():
        letters[letter] = 0
    letters[letter] += 1

#print(letters)
#exit
for key, value in letters.items():                  # unpacked each key and each belonging value
    print(f"{key} -> {value}")

#for key in letters.keys():
#   print(f"{key} -> {letters[key]}")              # letters[key] == value



