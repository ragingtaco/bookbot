with open("books/frankenstein.txt") as f:
    file_contents = f.read()
lowered = file_contents.lower()


def word_count(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count


def Character_count(text):
    letter_count = {}
    for letter in text:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count


def sort_on(dict):
    return dict["num"]


def LetterAmount(text):
    LetterCount = Character_count(text)
    Letters = []
    for Letter in LetterCount:
        if Letter.isalpha():
            Letters.append({"char": Letter,"num" : LetterCount[Letter]})
    WordCount = word_count(text)
    Letters.sort(key=sort_on, reverse=True)
    return Letters

Count = LetterAmount(lowered)
print("--- Begin report of books/frankenstein.txt ---")
print(f"{word_count(lowered)} words found in the document")
print()

for letter in Count:
    print(f"The {letter["char"]} character was found {letter["num"]} times")

print("--- End report ---")