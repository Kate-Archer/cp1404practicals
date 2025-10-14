"""
Word Occurrences
Estimate: 20 minutes
Actual:    minutes start 12:53
"""

word_to_count = {}
text = input("Give a string of words:")
words = text.split()
for word in words:
    #print(len(word))
    frequency = word_to_count.get(word, 0)
    word_to_count[word] = frequency + 1

max_length = max((len(word) for word in words))
for word in sorted(word_to_count):
    print(max_length)
    print(f"{word:{max_length}} : {word_to_count[word]}")
