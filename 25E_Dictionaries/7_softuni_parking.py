num = int(input())
register_users = {}

for i in range(num):
    command = input().split(" ")
    if command[0] == "register":
        username = command[1]
        license_plate = command[2]
        # username, license_plate = command[1], command[2]
        if username in register_users:
            print(f"ERROR: already registered with plate number {register_users[username]}")
        else:
            register_users[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
    elif command[0] == "unregister":
        username = command[1]
        if username not in register_users:
            print(f"ERROR: user {username} not found")
        else:
            register_users.pop(username)
            print(f"{username} unregistered successfully")

for username, license_plate in register_users.items():
    print(f"{username} => {license_plate}")


