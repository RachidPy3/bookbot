def count_words(book):
    words = book.split()
    return len(words)

def count_letters(book):
    lowered = book.lower()
    letters = {
        'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0,
        'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0,
        's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
    }
    for char in lowered:
        if char in letters:
            letters[char] += 1
    return letters

def print_report(letter_dict, word_count):
    print("--- Begin report of frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    for letter in letter_dict:
        print(f"the '{letter}' character was found {letter_dict[letter]} times")


def main():
    book = open("franklenstein.txt", "r")
    book_content = book.read()
    word_count = count_words(book_content)
    letter_count = count_letters(book_content)
    print_report(letter_count, word_count)
main()