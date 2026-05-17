#program to count the number of vowels in a file
file=open("sample.txt","r")
vowels=0
for line in file:
  for char in line:
    if char in "aeiouAEIOU":
      vowels+=1
print(f"the number of vowels is :{vowels}")
