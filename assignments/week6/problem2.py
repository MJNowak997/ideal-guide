import string

with open("alice.txt", "r") as f:
    text = f.read()

words = text.split()

count = {}
for word in words:
    count[word] = count.get(word, 0) + 1

sort = sorted(count.items())

with open("alice_words.txt", "w") as f:
    f.write("Word              Count\n")
    f.write("=======================\n")
    for word, count in sort:
        f.write(f"{word}          {count}\n")