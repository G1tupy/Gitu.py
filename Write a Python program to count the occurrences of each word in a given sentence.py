from collections import Counter
import re

def count_word_occurrences(sentence):
    # Remove punctuation and convert all words to lowercase
    words = re.findall(r'\b\w+\b', sentence.lower())
    
    # Count the occurrences of each word
    word_counts = Counter(words)
    return word_counts

# Given sentence
given_string = "To change the overall look of your document. To change the look available in the gallery"

# Count word occurrences and print the result
word_occurrences = count_word_occurrences(given_string)
for word, count in word_occurrences.items():
    print(f'Word "{word}" occurs {count} time(s)')