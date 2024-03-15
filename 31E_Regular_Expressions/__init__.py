import re

number_of_iterations = int(input())
for _ in range(number_of_iterations):
    data = input()
    pattern = r'(\@\#+)([A-Z][A-Za-z0-9]{4,}[A-Z])(\@\#+)'
    result = re.findall(pattern, data)
    # result = re.findall(pattern, data)            #връща TUTLES
    if not result:
        print('Invalid barcode')
    else:
        for res in result:
            extract_numbers = res.isdigit()
            if not extract_numbers:
                print('Product group: 00')
            else:
                print(f"Product group: {extract_numbers}")