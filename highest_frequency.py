#higest frequency count
s=input()
freq={}
for char in s:
    freq[char]=freq.get(char,0)+1
    maxcount=max(freq,key=freq.get)
print(freq[maxcount])
