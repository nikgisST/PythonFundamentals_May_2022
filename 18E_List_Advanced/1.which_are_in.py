first_list = input().split(", ")
second_list = input().split(", ")
substrings = []
for first_word in first_list:
    for second_word in second_list:
        if first_word in second_word and not first_word in substrings:
            substrings.append(first_word)
            break
print(substrings)


first_list = input().split(", ")
second_list = input().split(", ")
substrings = []
substrings = [x for x in first_list if any(x in w for w in second_list)]
print(substrings)