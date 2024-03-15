import re

dates = input()

pattern = r'(\d{2})([\/.-])([A-Z][a-z]{2})\2(\d{4})'

result = re.findall(pattern, dates)
for match in result:
    print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")





import re

text = input()
pattern = "\\b(?P<day>\\d{2})([-.\\/])(?P<month>[A-Z][a-z]{2})\\2(?P<year>\\d{4})\\b"

result = re.finditer(pattern, text)
for match in result:
    print(f"Day: {match.group('day')}, Month: {match.group('month')}, Year: {match.group('year')}")