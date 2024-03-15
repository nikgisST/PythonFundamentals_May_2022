class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

emails = []
line = input()
while line != "Stop":
    command = line.split(" ")
    sender, receiver, content = command[0], command[1], command[2]
    email = Email(sender, receiver, content)
    emails.append(email)
    line = input()
indices = list(map(int, input().split(', ')))
send_emails = [emails[int(x)].send() for x in indices]
#for x in send_emails:
    #emails[x].send()
for email in emails:
    print(email.get_info())







class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

emails = []
line = input()
while line != "Stop":
    command = line.split(" ")
    sender, receiver, content = command[0], command[1], command[2]
    email = Email(sender, receiver, content)
    emails.append(email)
    line = input()
send_emails = [int(x) for x in input().split(", ")]
for x in send_emails:
    emails[x].send()
for email in emails:
    print(email.get_info())








class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

emails = []
while True:
    command = input()
    if command == "Stop":
        break
    sender, receiver, content = command.split(" ")
    email = Email(sender, receiver, content)
    emails.append(email)
send_emails = [int(x) for x in input().split(", ")]
for x in send_emails:
    emails[x].send()
for email in emails:
    print(email.get_info())






class Email:
  def __init__(self, sender, receiver, content):
    self.sender = sender
    self.receiver = receiver
    self.content = content
    self.is_sent = False
  def send(self):
    self.is_sent = True
  def get_info(self):
    return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"
emails = []
line = input()
while line != "Stop":
    tokens = line.split(" ")
    email = Email(tokens[0], tokens[1], tokens[2])
    emails.append(email)
    line = input()
send_emails = list(map(lambda x: int(x), input().split(", ")))
for x in send_emails:
    emails[x].send()
for email in emails:
    print(email.get_info())