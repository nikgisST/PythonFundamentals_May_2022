employees = input().split(" ")
happiness_factor = int(input())
employees = list(map(lambda x: int(x) * happiness_factor, employees))
average_happiness = sum(employees) / len(employees)
filtered = list(filter(lambda x: x >= average_happiness, employees))
half_of_employees = len(employees) / 2
if len(filtered) >= half_of_employees:
    print(f"Score: {len(filtered)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(employees)}. Employees are not happy!")
