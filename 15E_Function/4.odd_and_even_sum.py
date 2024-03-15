def odd_even_sum(num):
    odds = sum([])
    evens = sum([])

    for i in num:
        if int(i) % 2 == 0:
            evens += int(i)
        else:
            odds += int(i)

    print(f"Odd sum = {odds}, Even sum = {evens}")


number = input()
odd_even_sum(number)




def odd_even_sum(number):
    even_sum = 0
    odd_sum = 0

    for element in str(number):
        if int(element) % 2 == 0:
            even_sum += int(element)
        else:
            odd_sum += int(element)

    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


num = int(input())
print(odd_even_sum(num))



def even_odd_sum(numbers, even, odd):
    for index in range(len(numbers)):
        current_number = int(numbers[index])
        if current_number % 2 == 0:
            even += current_number
        else:
            odd += current_number

    return f'Odd sum = {odd}, Even sum = {even}'


numbers = input()
even_sum = 0
odd_sum = 0
print(even_odd_sum(numbers, even_sum, odd_sum))