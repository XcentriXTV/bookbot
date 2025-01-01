def main():
    book_path = "books/frankenstein.txt"	# Path to the book you want to analyze
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    word_count = get_word_count(text)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    sorted_word_count = sorted(word_count.items(), key=lambda item: item[1], reverse=True)
    print("\nMost common words:")
    for word, count in sorted_word_count[:20]:
        print(f"The word '{word}' was found {count} times")
    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)

def get_word_count(text):
    d = {}
    for line in text.splitlines():
        words = line.split(" ")
        
        for word in words:
            if word in d:
                d[word] = d[word] + 1
            else:
                d[word] = 1
    return d


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(key=lambda item: item["char"])
    return sorted_list


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()