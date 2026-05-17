#program to find and print the longest word in a given text file.
file=open("document.txt","r")
longestword=""
for line in file:
    words=line.split()
    for word in words:
      if len(word)>len(longestword):
        longestword=word
print(longestword)
file.close()
