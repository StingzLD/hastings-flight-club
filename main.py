import data_manager

print("Welcome to Hastings Flight Club!\n"
      "We find the best flight deals and email them to you.\n")

first_name = input("What is your first name? ").title()
last_name = input("What is your last name? ").title()

email1 = "email1"
email2 = "email2"

while email1 != email2:
    email1 = input("What is your email? ").lower()
    if email1 == "quit" or email1 == "exit":
        exit()

    email2 = input("Please verify your email: ").lower()
    if email2 == "quit" or email2 == "exit":
        exit()

print("\nWelcome to Hastings Flight Club!")
print("""
The first rule of the Flight Club is there is DEFINITELY a Flight Club!
Tell everyone you know about it!
""")

data_manager.add_user(first_name, last_name, email1)
