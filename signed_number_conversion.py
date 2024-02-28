from number_conversion import binary_to_decimal

def signed_binary_fraction_to_octal(signed_binary_fraction):
    # Check if the input is integer binary
    if '.' not in signed_binary_fraction:
        integer_part = signed_binary_fraction
        fractional_part = ''
    else:
        # Separate integer and fractional parts
        integer_part, fractional_part = signed_binary_fraction.split('.')
    
    # Convert integer part to octal
    integer_octal = binary_to_octal(integer_part)
    
    # Convert fractional part to octal
    fractional_octal = ''
    if fractional_part:
        fractional_octal = fractional_binary_to_octal(fractional_part)
    
    # Combine integer and fractional parts
    octal_number = integer_octal + ('.' + fractional_octal if fractional_part else '')
    
    # Add '7' if negative
    if signed_binary_fraction[0] == '1':
        padding_length = len(integer_octal) % 3
        if padding_length == 0:
            integer_octal = '7' + integer_octal  # Pad '7' to complete the 3 digit length
        else:
            padding = '7' * (3 - padding_length)
            integer_octal = padding + integer_octal  # Pad '7's based on the remaining length
        octal_number = integer_octal + ('.' + fractional_octal if fractional_part else '')

    return octal_number


def signed_binary_to_decimal(binary):
    if binary[0] == '1':  # Check if the number is negative
        # Convert negative binary to positive binary
        positive_binary = ''
        for bit in binary[1:]:
            positive_binary += '1' if bit == '0' else '0'

        # Add 1 to the positive binary using the two's complement
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

        # Convert the positive result to decimal and negate it
        decimal = binary_to_decimal(result)
    else:
        # Positive binary, convert to decimal directly
        decimal = binary_to_decimal(binary)

    return decimal


def signed_binary_fraction_to_hex(signed_binary_fraction):
    # Check if the input is integer binary
    if '.' not in signed_binary_fraction:
        integer_part = signed_binary_fraction
        fractional_part = ''
    else:
        # Separate integer and fractional parts
        integer_part, fractional_part = signed_binary_fraction.split('.')
    
    # Convert integer part to hexadecimal
    integer_hex = binary_to_hex(integer_part)
    
    # Convert fractional part to hexadecimal
    fractional_hex = fractional_binary_to_hex(fractional_part)
    
    # Combine integer and fractional parts
    hex_number = integer_hex + ('.' + fractional_hex if fractional_part else '')
    
    # Add 'F' if negative
    if signed_binary_fraction[0] == '1':
        padding_length = len(integer_hex) % 4
        if padding_length == 0:
            integer_hex = 'F' + integer_hex  # Pad '7' to complete the 3 digit length
        else:
            padding = 'F' * (4 - padding_length)
            integer_hex = padding + integer_hex # Pad '7's based on the remaining length
        hex_number = integer_hex + ('.' + fractional_hex if fractional_part else '')

    return hex_number

def fractional_binary_to_octal(fractional_binary):
    # Convert
    fractional_octal = ''
    length = len(fractional_binary)
    # Padding
    while length % 3 != 0:
        fractional_binary += '0'
        length += 1
    for i in range(0, length, 3):
        # Group
        binary_group = fractional_binary[i:i+3]
        octal_digit = 0
        # Convert
        for bit in binary_group:
            octal_digit = octal_digit * 2 + int(bit)
        fractional_octal += str(octal_digit)
    
    return fractional_octal

def fractional_binary_to_hex(fractional_binary):
    # Convert
    fractional_hex = ''
    length = len(fractional_binary)
    # Padding
    while length % 4 != 0:
        fractional_binary += '0'
        length += 1
    for i in range(0, length, 4):
        # Group
        binary_group = fractional_binary[i:i+4]
        hex_digit = format(int(binary_group, 2), '01X')  # Convert binary group to hexadecimal
        fractional_hex += hex_digit
    
    return fractional_hex

def binary_to_octal(binary_number):
    # Check if the number is negative
    is_negative = False
    if '77' in binary_number:
        is_negative = True
    # Split into integer and fractional parts
    parts = binary_number.split('.')
    integer_part = parts[0]
    fractional_part = parts[1] if len(parts) > 1 else ''
    
    # Convert integer part to octal
    octal_integer = binary_to_octal_integer(integer_part)
    
    # Convert fractional part to octal
    octal_fractional = binary_to_octal_fractional(fractional_part)
    
    # Combine integer and fractional parts
    octal_number = octal_integer + ('.' + octal_fractional if fractional_part else '')
    
    # Add '7' if negative
    if is_negative:
        padding_length = len(octal_integer) % 3
        if padding_length == 0:
            octal_integer = '7' + octal_integer  # Pad '7' to complete the 3 digit length
        else:
            padding = '7' * (3 - padding_length)
            octal_integer = padding + octal_integer  # Pad '7's based on the remaining length
        octal_number = octal_integer + ('.' + octal_fractional if fractional_part else '')

    return octal_number

def binary_to_hex(binary_number):
    # Check if the number is negative
    is_negative = False
    if '1111' in binary_number:
        is_negative = True
    # Split into integer and fractional parts
    parts = binary_number.split('.')
    integer_part = parts[0]
    fractional_part = parts[1] if len(parts) > 1 else ''
    
    # Convert integer part to hexadecimal
    hex_integer = binary_to_hex(integer_part)
    
    # Convert fractional part to hexadecimal
    hex_fractional = binary_to_hex(fractional_part)
    
    # Combine integer and fractional parts
    hex_number = hex_integer + ('.' + hex_fractional if fractional_part else '')
    
    # Add 'F' if negative
    if is_negative:
        padding_length = len(hex_integer) % 4
        if padding_length == 0:
            hex_integer = 'F' + hex_integer  # Pad 'F' to complete the 4 digit length
        else:
            padding = 'F' * (4 - padding_length)
            hex_integer = padding + hex_integer # Pad 'F's based on the remaining length
        hex_number = hex_integer + ('.' + hex_fractional if fractional_part else '')

    return hex_number
