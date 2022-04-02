"""Menu to convert decimal to multiple bases (2 to 16)"""


def print_menu() -> None:
    print('\nMenu:')
    print('1. decimal to other base')
    print('2. quit')


def deci_to_other() -> None:
    """converts decimal to a specified base"""
    decimal = int(input('Enter number to be converted: '))
    base = int(input('Enter base to be converted to: '))
    letters = ["A", "B", "C", "D", "E", "F"]
    output = ""
    while decimal != 0:
        rem = decimal % base
        if rem > 9:
            rem = letters[rem - 10]
        else:
            rem = str(rem)
        output = rem + output
        decimal = decimal // base
    print(output)


def main() -> None:
    selected_quit = False
    input_line = None

    while not selected_quit:
        print_menu()
        command = int(input('\nEnter command: '))
        if command == 1:
            deci_to_other()
        elif command == 2:
            selected_quit = True


if __name__ == '__main__':
    main()