# positive lookbehind === (?<=\s)

import re

some_string = input()
pattern = r'(?<=\s)(([a-z0-9]+[\.\-\_a-z0-9]*)@[a-z\-]+(\.[a-z]+)+)\b'
matches = re.findall(pattern,some_string)
for match in matches:
    print(match[0])



some_string = input()
pattern = r'(?<=\s)(([a-z0-9]+[\.\-\_a-z0-9]*)@[a-z\-]+(\.[a-z]+)+)'
matches = re.findall(pattern,some_string)
for match in matches:
    print(match[0])




some_string = input()
pattern = r'\s(([a-z0-9]+[\.\-\_a-z0-9]*)@[a-z\-]+(\.[a-z]+)+)\b'
matches = re.findall(pattern,some_string)
for match in matches:
    print(match[0])