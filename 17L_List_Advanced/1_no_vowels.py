text = input()
vowels = ['a', 'u', 'e', 'i', 'o']
no_vowels = [ch for ch in text if ch.lower() not in vowels]
print(''.join(no_vowels))
