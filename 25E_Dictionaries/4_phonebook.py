phone_book = {}
while True:
    entry = input()
    if not "-" in entry:
        break
    # something = entry.split("-")
    # name = something[0]
    # phone = something[1]
    name, phone = entry.split("-")
    phone_book[name] = phone
for checking in range(int(entry)):
    searched_contact = input()
    if searched_contact in phone_book.keys():  # in phone_book():
        print(f"{searched_contact} -> {phone_book[searched_contact]}")
    else:
        print(f"Contact {searched_contact} does not exist.")
