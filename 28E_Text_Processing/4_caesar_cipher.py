text = input()
encrypted_text = []

for ch in text:
    three_position_forward = ord(ch) + 3
    encrypted_text.append(three_position_forward)
print(f"{''.join([chr(x) for x in encrypted_text])}")






def caesar_cipher(string):
    three_position_forward = ''
    for ch in string:
         three_position_forward += chr(ord(ch) + 3)
    return three_position_forward


text = input()
print(caesar_cipher(text))




print("".join([chr(ord(letter) + 3) for letter in input()]))