def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    
    return len(words)

def count_chars(text):
    characters = {}
    lowercase = text.lower()

    for char in lowercase:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    
    return characters

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_count = count_chars(text)
    
    print(char_count)

main()
