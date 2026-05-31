import json
import random
import string


VAULT_FILE = "vault.json"


def load_data():
    try:
        with open(VAULT_FILE, "r") as file:
            return json.load(file)
    except:
        return {}


def save_data(data):
    with open(VAULT_FILE, "w") as file:
        json.dump(data, file, indent=4)


def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(chars) for _ in range(length))


def add_password():
    data = load_data()

    website = input("Website: ")

    choice = input("Generate password automatically? (y/n): ")

    if choice.lower() == "y":
        password = generate_password()
        print(f"Generated Password: {password}")
    else:
        password = input("Enter password: ")

    data[website] = password
    save_data(data)

    print("Password saved successfully.")


def view_passwords():
    data = load_data()

    if not data:
        print("Vault is empty.")
        return

    for website, password in data.items():
        print(f"{website} --> {password}")


def search_password():
    data = load_data()

    website = input("Search website: ")

    if website in data:
        print(f"Password: {data[website]}")
    else:
        print("Website not found.")


def delete_password():
    data = load_data()

    website = input("Delete website: ")

    if website in data:
        del data[website]
        save_data(data)
        print("Deleted successfully.")
    else:
        print("Website not found.")


while True:

    print("\n===== PASSWORD MANAGER =====")
    print("1. Add Password")
    print("2. View Passwords")
    print("3. Search Password")
    print("4. Delete Password")
    print("5. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_password()

    elif choice == "2":
        view_passwords()

    elif choice == "3":
        search_password()

    elif choice == "4":
        delete_password()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")