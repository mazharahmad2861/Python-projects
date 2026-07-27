import re

def read_input_file(filename):
    try:
        file = open(filename, 'r')
        return file.read().strip()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return ""
    
# Write the code below
def display_results(total_words,search_word, word_frequency):
    print(f"Total Words: {total_words}")
    print(f"Frequency of '{search_word}': {word_frequency}")

def count_words_split(text):
    words = text.split()
    return words

def count_words_regex(text):
    words = re.findall(r'\b\w+\b', text)  # Extract words while ignoring punctuation
    return words

def word_frequency(words):
    search_word = input("Enter the word to search: ")
    word_freq = words.count(search_word)
    return word_freq, search_word

if __name__ == "__main__":
    filename = "input.txt"
    text = read_input_file(filename)

    if text:
        
        words = count_words_regex(text)
        total_words = len(words)
        word_freq, search_word = word_frequency(words)
        display_results(total_words, search_word, word_freq)