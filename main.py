import binary_operation
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
    if response.lower() in ['y', 'yes']:
        return True
    elif response.lower() in ['n', 'no']:
        return False
    else:
        return is_signed()
    
def twos_complement(binary_str):
    inverted = ''.join('1' if bit == '0' else '0' for bit in binary_str)
    twos_comp = bin(int(inverted, 2) + 1)[2:]
    return twos_comp.zfill(len(binary_str))


def binary_to_decimal(binary):
    decimal = 0.0
    is_negative = False

    if binary[0] == '1':
        is_negative = True
        # If it is two's complement, convert to positive decimal
        binary = twos_complement(binary[1:])

    if '.' in binary:
        integer_part, fractional_part = binary.split('.')

        # Convert integer part
        for digit in integer_part:
            decimal = decimal * 2 + int(digit)

        # Convert fractional part
        fractional_decimal = 0.0
        fractional_len = len(fractional_part)
        for i in range(fractional_len):
            fractional_decimal += int(fractional_part[i]) / (2 ** (i + 1))

        decimal += fractional_decimal

    else:
        # Convert whole binary number if no fractional part
        for digit in binary:
            decimal = decimal * 2 + int(digit)

    return -decimal if is_negative else decimal



def decimal_to_binary(decimal, length=0):
    if decimal == 0:
        return "0"

    is_negative = decimal < 0
    decimal = abs(decimal)

    integer_part = int(decimal)
    fractional_part = decimal - integer_part if decimal != int(decimal) else 0.0

    binary_integer = ""
    while integer_part > 0:
        binary_integer = str(integer_part % 2) + binary_integer
        integer_part //= 2

    binary_fractional = ""
    while fractional_part > 0:
        fractional_part *= 2
        bit = int(fractional_part)
        binary_fractional += str(bit)
        fractional_part -= bit

    binary_result = binary_integer + (("." + binary_fractional) if binary_fractional else "")

    if is_negative:
        binary_result = twos_complement(binary_result)

    if length > len(binary_result):
        padding = "0" * (length - len(binary_result))
        binary_result = padding + binary_result

    return binary_result

def decimal_to_octal(decimal):
    is_negative = False

    if decimal < 0:
        is_negative = True
        decimal = abs(decimal)

    integer_part = int(decimal)
    fractional_part = decimal - integer_part if decimal != int(decimal) else 0.0

    octal_integer = ""
    while integer_part > 0:
        octal_integer = str(integer_part % 8) + octal_integer
        integer_part //= 8

    if is_negative:
        octal_integer = '7' + octal_integer  # Ensure the first digit is 7 for negative numbers

    octal_fractional = ""
    for _ in range(8):
        fractional_part *= 8
        digit = int(fractional_part)
        octal_fractional += str(digit)
        fractional_part -= digit

    octal_result = octal_integer + ('.' + octal_fractional if octal_fractional else '')

    return octal_result.rstrip('0')  # Remove trailing zeros

def decimal_to_hexadecimal(decimal):
    is_negative = False

    if decimal < 0:
        is_negative = True
        decimal = abs(decimal)

    integer_part = int(decimal)
    fractional_part = decimal - integer_part if decimal != int(decimal) else 0.0

    hex_integer = ""
    while integer_part > 0:
        hex_integer = (str(integer_part % 16) if integer_part % 16 < 10 else chr(ord('A') + integer_part % 16 - 10)) + hex_integer
        integer_part //= 16

    hex_fractional = ""
    for _ in range(8):
        fractional_part *= 16
        digit = int(fractional_part)
        hex_fractional += (str(digit) if digit < 10 else chr(ord('A') + digit - 10))
        fractional_part -= digit

    hex_result = hex_integer + ('.' + hex_fractional if hex_fractional else '')

    return ('' + hex_result) if is_negative else hex_result

def binary_to_octal(binary):
    is_negative = False
    if binary[0] == '1':
        is_negative = True
        # If it is two's complement, convert to positive binary
        binary = twos_complement(binary[1:])

    integer_part, fractional_part = binary.split('.')

    # Convert integer part to decimal
    decimal_integer = binary_to_decimal(integer_part)

    # Convert fractional part to decimal
    fractional_decimal = 0.0
    fractional_len = len(fractional_part)
    for i in range(fractional_len):
        fractional_decimal += int(fractional_part[i]) / (2 ** (i + 1))

    # Combine integer and fractional parts
    decimal = decimal_integer + fractional_decimal

    # Convert decimal to octal
    octal_result = decimal_to_octal(decimal)

    return ('-' if is_negative else '') + octal_result.rstrip('0')  # Remove trailing zeros

def binary_to_hexadecimal(binary):
    is_negative = False
    if binary[0] == '1':
        is_negative = True
        # If it is two's complement, convert to positive binary
        binary = twos_complement(binary[1:])

    integer_part, fractional_part = binary.split('.')

    # Convert integer part to decimal
    decimal_integer = binary_to_decimal(integer_part)

    # Convert fractional part to decimal
    fractional_decimal = 0.0
    fractional_len = len(fractional_part)
    for i in range(fractional_len):
        fractional_decimal += int(fractional_part[i]) / (2 ** (i + 1))

    # Combine integer and fractional parts
    decimal = decimal_integer + fractional_decimal

    # Convert decimal to hexadecimal
    hexadecimal_result = decimal_to_hexadecimal(decimal)

    return ('-' if is_negative else '') + hexadecimal_result




def number_system_conversion():
    while True:
        print("\nNumber Conversion Menu:")
        print("1. Binary to X")
        print("2. Decimal to X")
        print("3. Octal to X")
        print("4. Hexadecimal to X")
        print("5. Exit")

        conversion_choice = input("Enter your selected option: ")
        if conversion_choice == '1':
            os.system('cls || clear')
            binary_input = input("Enter a binary number: ")
            if '.' in binary_input:
                integer_part, fractional_part = binary_input.split('.')
                decimal_integer = binary_to_decimal(integer_part)
                if decimal_integer is None:
                    print("Invalid binary number.")
                    continue
                decimal_fractional = 0.0
                fractional_len = len(fractional_part)
                for i in range(fractional_len):
                    decimal_fractional += int(fractional_part[i]) / (2 ** (i + 1))
                decimal_result = decimal_integer + decimal_fractional
            else:
                decimal_result = binary_to_decimal(binary_input)
                if decimal_result is None:
                    print("Invalid binary number.")
                    continue


            octal_result = decimal_to_octal(decimal_result)
            hexadecimal_result = decimal_to_hexadecimal(decimal_result)
            print(f"\nOUTPUT: ")
            print(f"\nDecimal: {decimal_result}")
            print(f"Octal: {octal_result}")
            print(f"Hexadecimal: {hexadecimal_result}")

        elif conversion_choice == '2':
            os.system('cls || clear')
            decimal_input = input("Enter a decimal number: ")
            if '.' in decimal_input:
                integer_part, fractional_part = decimal_input.split('.')
                decimal_result = int(integer_part)
                fractional_len = len(fractional_part)
                for i in range(fractional_len):
                    decimal_result += int(fractional_part[i]) / (10**(i+1))
            else:
                decimal_result = int(decimal_input)

            binary_result = decimal_to_binary(decimal_result)
            octal_result = decimal_to_octal(decimal_result)
            hexadecimal_result = decimal_to_hexadecimal(decimal_result)
            print(f"\nOUTPUT: ")
            print(f"\nBinary: {binary_result}")
            print(f"Octal: {octal_result}")
            print(f"Hexadecimal: {hexadecimal_result}")

        elif conversion_choice == '3':
            os.system('cls || clear')
            octal_input = input("Enter an octal number: ")

            is_negative = False
            if octal_input[0] == '-':
                is_negative = True
                octal_input = octal_input[1:]

            if '.' in octal_input:
                integer_part, fractional_part = octal_input.split('.')
                decimal_integer = 0
                for i in range(len(integer_part)):
                    decimal_integer = decimal_integer * 8 + int(integer_part[i])
                decimal_fractional = 0.0
                fractional_len = len(fractional_part)
                for i in range(fractional_len):
                    decimal_fractional += int(fractional_part[i]) / (8**(i+1))
                decimal_result = decimal_integer + decimal_fractional
            else:
                decimal_result = 0
                for digit in octal_input:
                    decimal_result = decimal_result * 8 + int(digit)

            decimal_result = -decimal_result if is_negative else decimal_result
            binary_result = decimal_to_binary(decimal_result)
            hexadecimal_result = decimal_to_hexadecimal(decimal_result)
            print(f"\nOUTPUT: ")
            print(f"\nBinary: {binary_result}")
            print(f"Decimal: {decimal_result}")
            print(f"Hexadecimal: {hexadecimal_result}")

        elif conversion_choice == '4':
            os.system('cls || clear')
            hex_input = input("Enter a hexadecimal number: ")

            is_negative = False
            if hex_input[0] == '-':
                is_negative = True
                hex_input = hex_input[1:]

            if '.' in hex_input:
                integer_part, fractional_part = hex_input.split('.')
                decimal_integer = 0
                hex_digits = "0123456789ABCDEF"
                for i in range(len(integer_part)):
                    decimal_integer = decimal_integer * 16 + hex_digits.index(integer_part[i].upper())
                decimal_fractional = 0.0
                fractional_len = len(fractional_part)
                for i in range(fractional_len):
                    decimal_fractional += hex_digits.index(fractional_part[i].upper()) / (16**(i+1))
                decimal_result = decimal_integer + decimal_fractional
            else:
                decimal_result = 0
                hex_digits = "0123456789ABCDEF"
                hex_input = hex_input.upper()

                for digit in hex_input:
                    decimal_result = decimal_result * 16 + hex_digits.index(digit)

            decimal_result = -decimal_result if is_negative else decimal_result
            binary_result = decimal_to_binary(decimal_result)
            octal_result = decimal_to_octal(decimal_result)
            print(f"\nOUTPUT: ")
            print(f"\nBinary: {binary_result}")
            print(f"Decimal: {decimal_result}")
            print(f"Octal: {octal_result}")

        elif conversion_choice == '5':
            break
        else:
            print("Invalid option. Please enter a valid choice.")

            
if __name__ == "__main__":
    while True:
        menu()
        option = int(input("Enter your option: "))
        if option == 1:
            while True:
                binary_operations_menu()
                binary_option = int(input("Enter your option for Binary Operations: "))
                if binary_option == 1:
                    os.system('cls || clear')
                    print('BINARY DIVISION')
                    binary1 = input("\nEnter the first binary number: ")
                    binary2 = input("Enter the second binary number: ")

                    if is_signed():
                        result = signed_binary_operation.division_binary(binary1, binary2)
                    else:
                        result = binary_operation.division_binary(binary1, binary2)

                    input(f"{binary1} / {binary2} = {result}")

                elif binary_option == 2:
                    os.system('cls || clear')
                    print('BINARY MULTIPLICATION')
                    binary1 = input("\nEnter the first binary number: ")
                    binary2 = input("Enter the second binary number: ")
                    
                    if is_signed():
                        result = signed_binary_operation.multiply_binary(binary1, binary2)
                    else:
                        result = binary_operation.multiply_binary(binary1,binary2)
                        
                    input(f"{binary1} * {binary2} = {result}")

                elif binary_option == 3:
                    os.system('cls || clear')
                    print('BINARY SUBTRACTION')
                    binary1 = input("\nEnter the first binary number: ")
                    binary2 = input("Enter the second binary number: ")

                    if is_signed():
                        result = signed_binary_operation.subtract_binary(binary1, binary2)
                    else:
                        result = binary_operation.subtract_binary(binary1, binary2)

                    input(result)

                elif binary_option == 4:
                    os.system('cls || clear')
                    print('BINARY ADDITION')
                    binary1 = input("\nEnter the first binary number: ")
                    binary2 = input("Enter the second binary number: ")

                    if is_signed():
                        result = signed_binary_operation.add_binary(binary1, binary2)
                    else:
                        result = binary_operation.add_binary(binary1, binary2)
                    input(f"{binary1} + {binary2} = {result}")

                elif binary_option == 5:
                    os.system('cls || clear')
                    print("2's COMPLEMENT")
                    binary1 = input("\nEnter the binary number: ")
                    result = binary_operation.complement(binary1)
                    input(result)

                else:
                    break
        elif option == 2:
            number_system_conversion()
        elif option == 3:
            break
        else:
            print("Invalid option. Please choose again.")