numbers_as_string = input().split(", ")
numbers_as_digit = [int(number) for number in numbers_as_string]
# numbers_as_digits = []
# for number in numbers_as_string:
#     numbers_as_digits.append(int(number))
print(f"Positive: {', '.join(str(number) for number in numbers_as_digit if number >= 0)}")


##########################################################################################################


numbers_as_string = input().split(", ")
print(f"Positive: {', '.join(number for number in numbers_as_string if int(number) >= 0)}")
print(f"Negative: {', '.join(number for number in numbers_as_string if int(number) < 0)}")
print(f"Even: {', '.join(number for number in numbers_as_string if int(number) % 2 == 0)}")
print(f"Odd: {', '.join(number for number in numbers_as_string if int(number) % 2 != 0)}")


##########################################################################################################


#функции се ползват, когато:
# 1) при промяна на данни
# 2) нещо ще се използва много пъти като вид операция


def positive_numbers(numbers):
    return [number for number in numbers if int(number) >= 0]


def negative_numbers(numbers):
    return [number for number in numbers if int(number) < 0]


def even_numbers(numbers):
    return [number for number in numbers if int(number) % 2 == 0]


def odd_numbers(numbers):
    return [number for number in numbers if int(number) % 2 != 0]


numbers_as_string = input().split(", ")
print(f"Positive: {', '.join(positive_numbers(numbers_as_string))}")
print(f"Negative: {', '.join(negative_numbers(numbers_as_string))}")
print(f"Even: {', '.join(even_numbers(numbers_as_string))}")
print(f"Odd: {', '.join(odd_numbers(numbers_as_string))}")

