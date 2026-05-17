# program that reads a file line by line and prints each line prefixed with its line number 
file = open("document.txt", "r")
count = 1  # Start counting at 1 for natural line numbers

for line in file:
    # Print the line number and the line text together
    # strip() removes extra blank lines from the file formatting
    print(f"{count}: {line.strip()}")
    count += 1

# Move close() outside the loop so it only runs when fully finished
file.close()
