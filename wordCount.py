#program to read a text file and count how many times the specific word "Python" appears in it.
file=open("document.txt","w+")
file.write("Python is a high-level, general-purpose programming language that is widely celebrated for its clean syntax, readability, and remarkable versatility. Created by Dutch programmer Guido van Rossum and first released in 1991, Python was intentionally named after the British comedy series Monty Python’s Flying Circus to keep the language fun and engaging. Today, it is one of the most popular programming languages globally, powering everything from simple automation scripts to complex artificial intelligence systems.")
count=0
file.seek(0)

for line in file:
    words=line.split()
    for i in words:
        if i.lower()=="python":
          count+=1
print(count)
file.close()
