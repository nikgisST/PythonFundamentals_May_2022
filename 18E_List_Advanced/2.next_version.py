version = [int(number) for number in input().split(".")]  # input().split(".")] това е лист
version[-1] += 1
for current_index in range(len(version) -1, -1, -1):
    if version[current_index] > 9:
        version[current_index] = 0
        if current_index - 1 >= 0:
            version[current_index - 1] += 1
print('.'.join(str(number) for number in version))       # .join works only with strings


version = input()
version = version.replace('.', '')
print(int(version) + 1)


# CTLR + ALT + L = PREFORMATING
