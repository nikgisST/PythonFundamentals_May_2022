import re

sentence = input()
word = input()
pattern = fr'\b{word}\b'
matches = re.findall(pattern, sentence, flags=re.IGNORECASE)
#matches = re.findall(pattern, sentence, flags=re.I)
print(len(matches))



# <img\sclass="size_(\d+x\d+)