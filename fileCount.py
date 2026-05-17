#program to find number of lines ,character,words from the file
line_count = 0
word_count = 0
char_count = 0


with open("sample.txt", "r") as f:
    for line in f:
        line_count += 1
        word_count += len(line.split())
        char_count += len(line)

print(f"Lines: {line_count}")
print(f"Words: {word_count}")
print(f"Characters: {char_count}")
