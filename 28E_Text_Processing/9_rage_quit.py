text = input().upper()
unique_symbols = ''
current_symbols = ''
repetitions = ''
for index in range(len(text)):
    if not text[index].isdigit():
        current_symbols += text[index]
    else:     #symbol is digit - time to multiply
        for check_next_symbols in range(index, len(text)):
            if not text[check_next_symbols].isdigit():
                break
            repetitions += text[check_next_symbols]
        repetitions = int(repetitions)
        unique_symbols += repetitions * current_symbols
        current_symbols = ''
        repetitions = ''
print(f"Unique symbols used: {len(set(unique_symbols))}")
print(unique_symbols)

#print(unique_symbols)
#print(set(unique_symbols))


def numbers():
    return [int(s) for s in range(1, 1001) if int(s) % 10 == 0]
print(numbers())