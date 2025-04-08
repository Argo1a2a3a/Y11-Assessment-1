import requests
words_text = requests.get("https://raw.githubusercontent.com/tabatkins/wordle-list/refs/heads/main/words").content
words = words_text.split()


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

letter_counts = {}
for word in words:
    for letter in letters:
        if letter in str(word):
            count = letter_counts.get(letter, 0)
            letter_counts[letter] = count + 1



sorted_letters = sorted(letter_counts.items(), key=lambda item: item[1], reverse=True)


for i, (letter, count) in enumerate(sorted_letters):
    if i == 0:
        print(f"The most common letter is '{letter}' with a count of {count}.")







