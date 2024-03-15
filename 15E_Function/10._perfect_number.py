def is_perfect(functioned_number):
    sum = 0
    for divisor in range(1, functioned_number):
        if functioned_number % divisor == 0:
            sum += divisor
    if functioned_number == sum:
        return "We have a perfect number!"
    return "It's not so perfect."

given_number = int(input())
print(is_perfect(given_number))