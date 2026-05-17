with open("sample.txt", "r") as infile, open("output.txt", "w") as outfile:
    for line in infile:
        words = line.split()
        new_words = []

        # Loop through words using their position index
        for index, word in enumerate(words):
            if index % 2 == 1:
                # Reverse the word if it is in an odd index (2nd, 4th, 6th word)
                new_words.append(word[::-1])
            else:
                # Keep the word as it is for even indexes (1st, 3rd, 5th word)
                new_words.append(word)

        # Join the words back into a line and write to the new file
        outfile.write(" ".join(new_words) + "\n")

print("Alternating words reversed successfully! Check 'output.txt'.")
