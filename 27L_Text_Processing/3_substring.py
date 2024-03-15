first_string = input()
second_string = input()
while first_string in second_string:
    second_string = second_string.replace(first_string, '')
print(second_string)




def replace_all_occurrences(first, second):
    while first in second:
        second = second.replace(first, '')
    return second


first_string = input()
second_string = input()
print(replace_all_occurrences(first_string, second_string))
# print(replace_all_occurrences(input(), input()))