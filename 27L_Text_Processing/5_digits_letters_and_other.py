text = input()
digits = ''
letters = ''
other = ''
for ch in text:
    if ch.isdigit():
        digits += ch
    elif ch.isalpha():
        letters += ch
    else:
        other += ch
print(digits)
print(letters)
print(other)






def get_digits(text):
    return ''.join([str(ch) for ch in text if ch.isdigit()])


def get_letters(text):
    return ''.join([ch for ch in text if ch.isalpha()])


def get_other(text):
    # return ''.join([ch for ch in text if not ch.isalpha() and not ch.isdigit()])
    return ''.join([ch for ch in text if not ch.isalnum()])

text = input()
print(get_digits(text))
print(get_letters(text))
print(get_other(text))





text = input()
dictionary = {"digits": [], "letters": [], "other": []}
for ch in text:
    if ch.isdigit():
        dictionary["digits"].append(ch)
    elif ch.isalpha():
        dictionary["letters"].append(ch)
    elif not ch.isalnum():
        dictionary["other"].append(ch)
print('\n'.join(f"{''.join(x)}" for x in dictionary.values()))