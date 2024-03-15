def length_is_valid(username):
    if 3 <= len(username) <= 16:
        return True
    return False

def char_are_valid(username):
    for char in username:
        if not (char.isalnum() or char == "-" or char == "_"):
            return False
    return True

def no_redundant_symbols(username):
    if not " " in username:
        return True
    return False

def is_valid(username):
    if length_is_valid(username) and char_are_valid(username) and no_redundant_symbols(username):
        return True
    return False


usernames = input().split(", ")
for username in usernames:
    if is_valid(username):
        print(username)




usernames = input().split(", ")
for username in usernames:
    valid = True
    if not 3 <= len(username) <= 16:
        valid = False
        continue
    for char in username:
        if not char.isalnum() or char == "-" or char == "_":
            valid = False
            continue
    if " " in username:
        valid = False
        continue

    if valid:
        print(username)