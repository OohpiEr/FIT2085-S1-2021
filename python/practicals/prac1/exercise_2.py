"""Menu to convert decimal to binary and decimal to hexadecimal"""


def print_menu() -> None:
    print('\nMenu:')
    print('1. decimal to binary')
    print('2. decimal to hex')
    print('3. quit')


def deci_to_binary() -> None:
    """converts decimal to binary"""
    decimal = int(input('Enter number to be converted: '))
    binary_output = ""
    while decimal != 0:
        rem = decimal % 2
        binary_output = str(rem) + binary_output
        decimal = decimal // 2
    print(binary_output)


def deci_to_hex() -> None:
    """converts decimal to hex"""
    decimal = int(input('Enter number to be converted: '))
    hex_letters = ["A", "B", "C", "D", "E", "F"]
    hex_output = ""
    while decimal != 0:
        rem = decimal % 16
        if rem > 9:
            rem = hex_letters[rem - 10]
        else:
            rem = str(rem)
        hex_output = rem + hex_output
        decimal = decimal // 16
    print(hex_output)


def main() -> None:
    selected_quit = False
    input_line = None

    while not selected_quit:
        print_menu()
        command = int(input('\nEnter command: '))
        if command == 1:
            deci_to_binary()
        elif command == 2:
            deci_to_hex()
        elif command == 3:
            selected_quit = True


if __name__ == '__main__':
    main()
