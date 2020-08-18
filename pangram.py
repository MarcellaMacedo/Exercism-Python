
def is_pangram(sentence):
    return len(set(letter.lower()
                   for letter in sentence
                   if letter.isalpha())) == 26
