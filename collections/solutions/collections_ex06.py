""" A Solution For collections_ex06

    Rewrite collections_ex02 to count the frequency of each
    word in the user's input.
    • A dict provides the perfect data structure for this problem.
    • Let the words be the keys, and let the counts be the values.
    • Print the results sorted by the words.
    • Finally, print the results sorted by the counts.
"""
words = {}

prompt = "Enter a some text (or just the word 'end' to quit) "
while True:
    data = input(prompt)
    if data == "end":
        break

    word_list = data.split()
    for word in word_list:
        words[word] = words.get(word, 0) + 1

key_list = list(words.keys())

print()
print("Words and count sorted by Words (the key)")
key_list.sort()
for word in key_list:
    print(word, words[word])

print("Words and Word count sorted by Word Count (the value)")

key_list.sort(key=words.get)
for word in key_list:
    print(word, words[word])
