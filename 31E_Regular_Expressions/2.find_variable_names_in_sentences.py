# [\w] == [a-zA-Z0-9_]

import re

sentence = input()
pattern = r'\b_([A-Za-z0-9]+)\b'
#pattern = '_([A-Za-z0-9]+)'
matches = re.findall(pattern,sentence)
print(",".join(matches))