import binary_operation
import number_conversion
import signed_binary_operation
import os

def binary_operations_menu():
    os.system("cls || clear")
    print("\nBinary Operations Menu")
    print("[1] Division")
    print("[2] Multiplication")
    print("[3] Subtraction")
    print("[4] Addition")
    print("[5] Negative (2's Complement)")

def number_conversion_menu():
    os.system("cls || clear")
    print("\nNumber Conversion Menu")
    print("[1] Binary to X")
    print("[2] Decimal to X")
    print("[3] Octal to X")
    print("[4] Hexa to X")

def menu():
    os.system("cls || clear")
    print("Main Menu")
    print("\n[1] Binary Operations")
    print("[2] Number System Conversion")
    print("[3] Exit")

def is_signed():
    response = input("Is it signed? [y/n]: ")
    if response in ['y', 'Y', 'yes', 'YES', '1']:
        return True
    elif response in ['n', 'N', 'no', 'NO', '0']:
        return False
    else:
        is_signed()

while True:
    menu()
    option = int(input("Enter your option: "))

    if option == 1:
        binary_operations_menu()
        binary_option = int(input("Enter your option for Binary Options: "))
        if binary_option == 1:
            os.system('cls || clear')
            print('<<< BINARY DIVISION >>>')
            binary1 = input("Enter the first binary number: ")
            binary2 = input("Enter the second binary number: ")

            if is_signed():
                result = signed_binary_operation.division_binary(binary1, binary2)
            else:
                result = binary_operation.division_binary(binary1, binary2)

            input(f"{binary1} / {binary2} = {result}")

        elif binary_option == 2:
            os.system('cls || clear')
            print('<<< BINARY MULTIPLICATION >>>')
            binary1 = input("Enter the first binary number: ")
            binary2 = input("Enter the second binary number: ")
            result = binary_operation.multiply_binary(binary1,binary2)
            input(f"{binary1} * {binary2} = {result}")

        elif binary_option == 3:
            os.system('cls || clear')
            print('<<< BINARY SUBTRACTION >>>')
            binary1 = input("Enter the first binary number: ")
            binary2 = input("Enter the second binary number: ")

            if is_signed():
                result = signed_binary_operation.subtract_binary(binary1, binary2)
            else:
                result = binary_operation.subtract_binary(binary1, binary2)

            input(result)

        elif binary_option == 4:
            os.system('cls || clear')
            print('<<< BINARY ADDITION >>>')
            binary1 = input("Enter the first binary number: ")
            binary2 = input("Enter the second binary number: ")

            if is_signed():
                result = signed_binary_operation.add_binary(binary1, binary2)
            else:
                result = binary_operation.add_binary(binary1, binary2)
            input(f"{binary1} + {binary2} = {result}")

        elif binary_option == 5:
            os.system('cls || clear')
            print("<<< 2's COMPLEMENT >>>")
            binary1 = input("Enter the binary number: ")
            result = binary_operation.complement(binary1)
            input(result)

        else:
            menu()

    elif option == 2:
        while True:
            number_conversion_menu()
            number_conversion_option = int(input("Enter your option for Number System Conversions:"))
            if number_conversion_option == 1:
                binary = input("Enter a binary number: ")
                decimal = number_conversion.binary_to_decimal(binary)
                octal = number_conversion.decimal_to_octal(decimal)
                hexadecimal = number_conversion.decimal_to_hexadecimal(decimal)
                print(f"Binary: {binary}")
                print(f"Decimal: {decimal}")
                print(f"Octal: {octal}")
                print(f"Hexadecimal: {hexadecimal}")
                input("Press Enter to continue...")
                os.system("cls || clear")

            elif number_conversion_option == 2:
                decimal = float(input("Enter a decimal number: "))
                binary = number_conversion.decimal_to_binary(int(decimal))
                octal = number_conversion.decimal_to_octal(int(decimal))
                hexadecimal = number_conversion.decimal_to_hexadecimal(int(decimal))
                print(f"Decimal: {decimal}")
                print(f"Binary: {binary}")
                print(f"Octal: {octal}")
                print(f"Hexadecimal: {hexadecimal}")
                input("Press Enter to continue...")
                os.system("cls || clear")

            elif number_conversion_option == 3:
                octal = input("Enter an octal number: ")
                binary = number_conversion.octal_to_binary(octal)
                decimal = number_conversion.octal_to_decimal(octal)
                hexadecimal = number_conversion.octal_to_hexadecimal(octal)

                print(f"Octal: {octal}")
                print(f"Binary: {binary}")
                print(f"Decimal: {decimal}")
                print(f"Hexadecimal: {hexadecimal}")
                input("Press Enter to continue...")
                os.system("cls || clear")

            elif number_conversion_option == 4:
                hexadecimal = input("Enter a hexadecimal number: ")
                binary = number_conversion.hexadecimal_to_binary(hexadecimal)
                decimal = number_conversion.hexadecimal_to_decimal(hexadecimal)
                octal = number_conversion.hexadecimal_to_octal(hexadecimal)

                print(f"Hexadecimal: {hexadecimal}")
                print(f"Binary: {binary}")
                print(f"Decimal: {decimal}")
                print(f"Octal: {octal}")
                input("Press Enter to continue...")
                os.system("cls || clear")

            elif number_conversion_option == 5:
                break

    elif option == 3:
        exit()

    else:
        menu()
