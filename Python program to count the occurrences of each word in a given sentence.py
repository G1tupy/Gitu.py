from collections import Counter

def count_word_occurrences(sentence):
    # Split the sentence into words and count occurrences
    word_counts = Counter(sentence.split())
    return word_counts

# Example sentence
sentence = "This is a sample sentence. This sentence is for testing purposes."

# Count word occurrences and print the result
word_occurrences = count_word_occurrences(sentence)
for word, count in word_occurrences.items():
    print(f'Word "{word}" occurs {count} time(s)')