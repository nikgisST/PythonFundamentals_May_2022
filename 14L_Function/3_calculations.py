import operator

def solve(a, b, operation):
    solve_dict = {'multiply': operator.mul, 'divide': operator.truediv,
                  'add': operator.add, 'subtract': operator.sub}
    return int(solve_dict[operation](a, b))

type_command = input()
first_number = int(input())
second_number = int(input())
print(solve(first_number, second_number, type_command))



def solve(a, b, operator):
    result = None
    if operator == 'multiply':
        result = a * b
    elif operator == 'divide':
        result = int(a / b)
    elif operator == 'add':
        result = a + b
    elif operator == 'subtract':
        result = a - b
    return result


type_command = input()
first_number = int(input())
second_number = int(input())
print(solve(first_number, second_number, type_command))
