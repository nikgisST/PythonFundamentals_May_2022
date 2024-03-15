list_of_numbers = input().split()
#print(list_of_numbers) превръща с split полученият стринг се превръща в лист, разделен с интервал (от int се превръщат в str)
opposite_numbers = []
for element in list_of_numbers:
    opposite_numbers.append(-int(element))
print(opposite_numbers)


list_of_numbers = input().split()
opposite_numbers = []
for current_index in range(len(list_of_numbers)):
    current_number = int(list_of_numbers[current_index])
    opposite_numbers.append(-current_number)
print(opposite_numbers)
