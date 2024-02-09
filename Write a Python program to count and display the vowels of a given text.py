def count_and_display_vowels(text):
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    vowel_list = []

    for char in text:
        if char in vowels:
            vowel_count += 1
            vowel_list.append(char)

    print(f"Number of vowels: {vowel_count}")
    print("Vowels:", ', '.join(vowel_list))

# Given string
given_string = "Welcome to Python Training"

# Call the function to count and display vowels
count_and_display_vowels(given_string)
