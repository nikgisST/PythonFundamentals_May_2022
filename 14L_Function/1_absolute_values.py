numbers = input().split(' ')
abs_numbers = []
for each_num in numbers:
    abs_numbers.append(abs(float(each_num)))
print(abs_numbers)




numbers = list(map(float, input().split(' ')))
result = [abs(num) for num in numbers]
print(result)





def abs_numbers(nums):
    result = [abs(num) for num in nums]
    return result
numbers = list(map(float, input().split(' ')))
print(abs_numbers(numbers))

