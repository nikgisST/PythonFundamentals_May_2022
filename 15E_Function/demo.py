def add_number(a,b):
    pass

print(add_number(3,4))

#тук функциите винаги връщат нещо - в тази задача св принтира None което не отговаря нито на False нито на True


#палиндром:
print('\n'.join([str(n == n[::-1]) for n in input().split(",")]))