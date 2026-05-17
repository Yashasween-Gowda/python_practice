#program that reads a file and copies its content to a new file, but converts every single letter to uppercase.
file=open("document.txt","r")
content=file.read()
copyfile=open("copyfile.txt","w")
copyfile.write(content.upper())
copyfile.close
file.close
