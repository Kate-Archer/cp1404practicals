"""
Word Occurrences
Estimate: 20 minutes
Actual: 18 minutes
"""

# Add dictionary for words to count (lowercase because it is not a global variable, it changes)
word_to_count = {}
# Split the text input, count the frequency of each word and print the count next to the word
text = input("Please write a sentence of text:").lower()
words = text.split()
for word in words:
    word_frequency = word_to_count.get(word, 0)
    word_to_count[word] = word_frequency + 1

max_length_word = max((len(word) for word in words))
for word in sorted(word_to_count):
    print(f"{word:{max_length_word}} : {word_to_count[word]}")
