def signed_fractional_decimal_to_binary_octal_hexadecimal(decimal):
    # Check if the number is negative
    is_negative = decimal < 0
    decimal = abs(decimal)

    # Separate the integer and fractional parts
    integer_part = int(decimal)
    fractional_part = decimal - integer_part

    # Convert integer part to binary, octal, and hexadecimal
    binary_integer = bin(integer_part)[2:]
    octal_integer = oct(integer_part)[2:]
    hexadecimal_integer = hex(integer_part)[2:]

    # Convert fractional part to binary
    binary_fractional = ""
    while fractional_part != 0:
        fractional_part *= 2
        bit = int(fractional_part)
        binary_fractional += str(bit)
        fractional_part -= bit
    binary_fractional = "." + binary_fractional if binary_fractional else ""

    # Combine the integer and fractional parts for each base
    binary_result = binary_integer + binary_fractional
    octal_result = octal_integer + binary_fractional
    hexadecimal_result = hexadecimal_integer + binary_fractional

    # Add negative sign if necessary
    if is_negative:
        binary_result = "-" + binary_result
        octal_result = "-" + octal_result
        hexadecimal_result = "-" + hexadecimal_result

    return binary_result, octal_result, hexadecimal_result

# Example usage
decimal = -3.625
binary, octal, hexadecimal = signed_fractional_decimal_to_binary_octal_hexadecimal(decimal)
print(f"Decimal: {decimal}\nBinary: {binary}\nOctal: {octal}\nHexadecimal: {hexadecimal}")
