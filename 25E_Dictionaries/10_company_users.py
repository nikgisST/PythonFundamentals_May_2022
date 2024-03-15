companies = {}
command = input().split(" -> ")
while command[0] != "End":
    # companies = command[0]
    # id = command[1]
    company, id = command
    if company in companies.keys():
        if id not in companies[company]:
            companies[company].append(id)
    else:
        # companies[company] = []
        # companies[company].append(id)
        companies[company] = [id]

    command = input().split(" -> ")

for company in companies.keys():          # for company in companies:
    print(f"{company}")

    for employee in companies[company]:
        print(f"-- {employee}")

