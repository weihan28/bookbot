def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
        wc = get_word_count(file_contents)
        char_int = count_letters(file_contents)
        print_report(path, wc, char_int)
            
def print_report(path, wc, char_int) -> None:
    print(f"--- Begin report of {path} ---")
    print(f"{wc} words found in the document\n")
    for c, count in sorted(char_int.items()):
        print(f"The '{c}' character was found {count} times")
    print(f"--- End report ---")


def get_word_count(str) -> int:
    words = str.split()
    return len(words)


def count_letters(str) -> dict:
    char_int = dict()
    for c in str:
        low_c = c.lower()
        if not low_c.isalpha():
            continue
        if low_c in char_int:
            char_int[low_c] += 1
        else:
            char_int[low_c] = 0
    return char_int


if __name__ == '__main__':
    main()