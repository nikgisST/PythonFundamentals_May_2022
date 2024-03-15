def type_of_grades(fun_grade):
    result = None
    #result = ''
    #if 2.00 and fun_grade <= 2.99 :
    if 2 <= fun_grade <= 2.99:
        result = 'Fail'
    #elif fun_grade >= 3.00 and fun_grade <= 3.49:
    elif 3 <= fun_grade <= 3.49:
        result = 'Poor'
    elif 3.50 <= fun_grade <= 4.49:
        result = 'Good'
    elif 4.50 <= fun_grade <= 5.49:
        result = 'Very Good'
    elif 5.50 <= fun_grade <= 6:
        result = 'Excellent'
    return result


score = float(input())
print(type_of_grades(score))




def type_of_grades(fun_grade):
    #if 2.00 and fun_grade <= 2.99 :
    if 2 <= fun_grade <= 2.99:
        return 'Fail'
    #elif fun_grade >= 3.00 and fun_grade <= 3.49:
    elif 3 <= fun_grade <= 3.49:
        return 'Poor'
    elif 3.50 <= fun_grade <= 4.49:
        return 'Good'
    elif 4.50 <= fun_grade <= 5.49:
        return 'Very Good'
    elif 5.50 <= fun_grade <= 6:
        return 'Excellent'


score = float(input())
print(type_of_grades(score))