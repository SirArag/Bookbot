def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    file_contents_lowercase = file_contents.lower()
    
    words = file_contents.split()
    count = len(words)

    letter_count = {}
    for char in file_contents_lowercase:
        letter_count[char] = letter_count.get(char, 0) + 1

    print("--- Begin report of books/frankenstein.txt ---")
    print(count, "words found in the document")
    for char in sorted(letter_count.keys()):
        if char.isalpha() == True:
            print(f"The '{char}' character was found {letter_count[char]} times")

main()