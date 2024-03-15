import re

pattern = '\d+'
line = input()
while True:
    if line:
        matches = re.findall(pattern, line)
        if matches:
            print(' '.join(matches), end= " ")
        line = input()
    else:
        break




import re

pattern = r'\d+'
line = input()
while line:
    if line:
        matches = re.findall(pattern, line)
        if matches:
            print(' '.join(matches), end= " ")
        line = input()
    else:
        break