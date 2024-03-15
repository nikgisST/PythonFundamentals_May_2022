import re


number_of_barcodes = int(input())
for _ in range(number_of_barcodes):
    data = input()
    pattern = r'(\@\#+)([A-Z][A-Za-z0-9]{4,}[A-Z])(\@\#+)'
    result = re.match(pattern, data)
    # result = re.finditer(pattern, data)
    # for el in result:
    #     print(el.group())                     ако не добавим group тук резултатът е същият като с match - MATCH OBJECTS

    # result = re.search(pattern, data)
    #     print(result.group())                     ако не добавим group тук резултатът е същият като с match - MATCH OBJECTS
    if not result:
        print('Invalid barcode')
    else:
        extract_numbers = re.findall('\d', result.group())
        if not extract_numbers:
            print('Product group: 00')
        else:
            print(f"Product group: {''.join(extract_numbers)}")