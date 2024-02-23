def binary_to_decimal(binary):
    decimal = 0
    binary = binary.replace(" ", "")  # Remove spaces from the binary string
    for i in range(len(binary)):
        decimal += int(binary[len(binary) - 1 - i]) * (2**i)
    return decimal

def twos_complement(binary):
    if binary[0] == '1':
        # Convert negative binary to positive binary
        positive_binary = ''
        for bit in binary:
            positive_binary += '1' if bit == '0' else '0'

        # Add 1 to the positive binary
        carry = 1
        result = ''
        for bit in positive_binary[::-1]:
            if bit == '1' and carry == 1:
                result = '0' + result
            elif bit == '0' and carry == 1:
                result = '1' + result
                carry = 0
            else:
                result = bit + result

        # Convert the result to decimal and make it negative
        return -int(result, 2)
    else:
        # Positive binary, convert to decimal directly
        return int(binary, 2)

def decimal_to_binary(decimal):
    if decimal == 0:
        return "0"
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary

def decimal_to_octal(decimal):
    octal = ""
    while decimal != 0:
        octal = str(decimal % 8) + octal
        decimal //= 8
    return octal

def decimal_to_hexadecimal(decimal):
    hexadecimal = ""
    while decimal != 0:
        remainder = decimal % 16
        if remainder < 10:
            hexadecimal = str(remainder) + hexadecimal
        else:
            hexadecimal = chr(ord('A') + remainder - 10) + hexadecimal
        decimal //= 16
    return hexadecimal

def octal_to_decimal(octal):
    decimal = 0
    for i in range(len(octal)):
        decimal += int(octal[len(octal) - 1 - i]) * (8**i)
    return decimal

def octal_to_binary(octal):
    decimal = octal_to_decimal(octal)
    return decimal_to_binary(decimal)

def octal_to_hexadecimal(octal):
    decimal = octal_to_decimal(octal)
    return decimal_to_hexadecimal(decimal)

def hexadecimal_to_decimal(hexadecimal):
    decimal = 0
    for i in range(len(hexadecimal)):
        digit = hexadecimal[len(hexadecimal) - 1 - i]
        if '0' <= digit <= '9':
            decimal += int(digit) * (16**i)
        else:
            decimal += (ord(digit.upper()) - ord('A') + 10) * (16**i)
    return decimal


def hexadecimal_to_binary(hexadecimal):
    decimal = hexadecimal_to_decimal(hexadecimal)
    return decimal_to_binary(decimal)

def hexadecimal_to_octal(hexadecimal):
    decimal = hexadecimal_to_decimal(hexadecimal)
    return decimal_to_octal(decimal)
