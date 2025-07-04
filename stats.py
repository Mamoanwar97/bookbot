def get_words(text):
    return text.split()

def get_word_count(words):
    return len(words)

def get_letter_count(text):
    letter_count = {}
    for letter in text:
        if letter.isalpha():
            letter = letter.lower()
            letter_count[letter] = letter_count.get(letter, 0) + 1
    return letter_count

def sort_on(items):
    return items["num"]

def display_letter_count(letter_count):
    letter_count_list = []
    for letter, count in letter_count.items():
        letter_count_list.append({"letter": letter, "num": count})
    letter_count_list.sort(reverse=True, key=sort_on)
    return letter_count_list