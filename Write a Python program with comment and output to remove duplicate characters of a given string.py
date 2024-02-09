def remove_duplicates(input_string):
    # Initialize an empty string to store unique characters
    unique_chars = ''

    # Iterate through each character in the input string
    for char in input_string:
        # If the character is not already in the unique_chars string
        if char not in unique_chars:
            # Add it to the unique_chars string
            unique_chars+=char

    return unique_chars

# Example input
input_string = "String and String Function"

# Remove duplicates from the input string and print the result
result = remove_duplicates(input_string)
print(result)
