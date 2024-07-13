# Початковий бот-асистент (без збереження у файл): 
# зберігає ім'я та номер телефону (у пам’яті), 
# знаходить номер телефону за ім'ям, 
# змінює записаний номер телефону, 
# виводить в консоль всі записи, які збереженні
from functools import wraps


def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            if inner.__name__ == 'add_contact' or inner.__name__ == 'change_contact':
                return "Enter the argument for the command: name and phone."
            else:
                return "ValueError"
        except KeyError:                    #не смог вызвать эту ошибку
            return "Contact not found"
        except IndexError:
            if inner.__name__ == 'phone_show':
                return "Enter the argument for the command: name."
            else:
                return "IndexError"

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error

def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return "Contact already exists"
    else:
        contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
    else:
        return "Contact not found"
    return "Contact updated."

@input_error
def phone_show(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found"

def main():
    print("Welcome to the assistant bot!")
    contacts = {}
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case ("close" | "exit"):
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, contacts))
            case "change":
                print(change_contact(args, contacts))
            case "phone":
                print(phone_show(args, contacts))
            case "all":
                print(contacts)
            case _:
                print("Invalid command. Available commands: add, change, phone, all, close/exit")


if __name__ == "__main__":
    main()
