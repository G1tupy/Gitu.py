def count_chars_digits_symbols(input_string):
    chars = sum(1 for char in input_string if char.isalpha())
    digits = sum(1 for char in input_string if char.isdigit())
    symbols = len(input_string) - chars - digits

    return f"Chars = {chars} Digits = {digits} Symbol = {symbols}"

# Example input
input_string = "P@#yn26at^&i5ve"

result = count_chars_digits_symbols(input_string) #Count characters, digits, and symbols in the input string and print the result
print(result)
