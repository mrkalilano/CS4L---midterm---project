def binary_to_decimal_fractional():
    def binary_to_decimal(binary):
        sign = -1 if binary[0] == '1' else 1
        decimal = 0
        for digit in binary[1:]:
            decimal = decimal * 2 + int(digit)
        return sign * decimal

    binary_input = input("Enter a binary number: ")
    if '.' in binary_input:
        integer_part, fractional_part = binary_input.split('.')
        decimal_integer = binary_to_decimal(integer_part)
        decimal_fractional = 0.0
        fractional_len = len(fractional_part)
        for i in range(fractional_len):
            decimal_fractional += int(fractional_part[i]) / (2**(i+1))
        decimal_result = decimal_integer + decimal_fractional
    else:
        decimal_result = binary_to_decimal(binary_input)
    
    return decimal_result
