def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except (KeyError, ValueError, IndexError) as f:
            return str(f)

    return inner


def handle_hello():
    return "How can I help you?"


def handle_add(name, phone, contacts):
    if len(name.strip()) == 0 or len(phone.strip()) == 0:
        raise ValueError("Please enter both name and phone number")
    contacts[name.lower()] = phone
    return f"Added contact {name} with phone {phone}"


def handle_change(name, phone, contacts):
    if name.lower() not in contacts:
        raise KeyError(f"{name} is not in contacts")
    contacts[name.lower()] = phone
    return f"Changed phone for contact {name} to {phone}"


def handle_phone(name, contacts):
    if name.lower() not in contacts:
        raise KeyError(f"{name} is not in contacts")
    return contacts[name.lower()]


def handle_show_all(contacts):
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])


def main():
    contacts = {}

    while True:
        command = input("Enter a command: ").lower()
        if command == "hello":
            print(handle_hello())
        elif command == '.':
            break
        elif command.startswith("add"):
            try:
                name, phone = command.split()[1:]
                print(handle_add(name, phone, contacts))
            except ValueError as e:
                print(str(e))
        elif command.startswith("change"):
            try:
                name, phone = command.split()[1:]
                print(handle_change(name, phone, contacts))
            except (KeyError, ValueError) as e:
                print(str(e))
        elif command.startswith("phone"):
            try:
                name = command.split()[1]
                print(handle_phone(name, contacts))
            except KeyError as e:
                print(str(e))
        elif command == "show all":
            print(handle_show_all(contacts))
        elif command in ("good bye", "close", "exit",):
            print("Good bye!")
            break
        else:
            print("Unknown command. Please try again.")


if __name__ == '__main__':
    main()
