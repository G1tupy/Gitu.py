def remove_duplicates(input_string):
    # Create an empty set to keep track of seen characters
    seen = set()
    # Initialize an empty list to store unique characters in order
    output = []

    # Iterate through each character in the input string
    for char in input_string:
        # If the character is not already in the set of seen characters
        if char not in seen:
            # Add it to the set to mark it as seen
            seen.add(char)
            # Add the character to the output list
            output.append(char)

    # Join the characters in the output list to form the final string
    return ''.join(output)

# Example input
input_string = "String and String Function"

# Remove duplicates from the input string and print the result
result = remove_duplicates(input_string)
print(result)
