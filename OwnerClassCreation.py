class Owner:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"Owner(name={self.name}, email={self.email})"

# Prompt the user to enter the owner's name and email
name = input("Enter the owner's name: ")
email = input("Enter the owner's email: ")

# Create an Owner object
owner = Owner(name, email)

# Print the Owner object
print(owner)