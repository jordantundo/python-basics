"""
Practice Project: Simple Contact Book 📖

This project combines classes, functions, lists, and file operations.
"""

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def display_contact(self):
        print(f"Name: {self.name}, Phone: {self.phone}")

# Create a few contacts
contact_list = [
    Contact("Alice", "123-456-7890"),
    Contact("Bob", "987-654-3210"),
]

# Display all contacts
for contact in contact_list:
    contact.display_contact()

# Save contacts to a file
with open("contacts.txt", "w") as file:
    for contact in contact_list:
        file.write(f"{contact.name},{contact.phone}\n")

print("\nContacts have been saved to 'contacts.txt'.")