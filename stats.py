def get_book_text(path):
    with open(path) as file:
        content = file.read()
        return content


def count_words(path):
    text = get_book_text(path)
    words = text.split()
    num_words = len(words)
    return f"{num_words} words found in the document"


def count_characters(path):
    text = get_book_text(path)
    lower_text = text.lower()
    characters = {}

    for word in lower_text:
        if word in characters:
            characters[word] += 1
        else:
            characters[word] = 1
    return characters


def sort_dict(path):
    total_words = count_words(path)
    dict_to_sort = count_characters(path)
    output_lines = []

    for key in sorted(dict_to_sort, key=dict_to_sort.get, reverse=True):
        if key.isalpha():
            output_lines.append(f"{key}: {dict_to_sort[key]}")
    result = "\n        ".join(output_lines)

    report_message = f"""
        ============ BOOKBOT ============
        Analyzing book found at books/frankenstein.txt...
        ----------- Word Count ----------
        Found {total_words} total words
        --------- Character Count -------
        {result}
        ============= END =============== """

    return report_message
