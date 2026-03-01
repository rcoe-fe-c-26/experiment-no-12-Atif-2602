# AIM: Develop a Python program that reads a text file and
# prints words of specified lengths (e.g., three, four,
# five, etc.) found within the file.
# Coder:Qureshi Atif

print("--- Extracting Words from Text File ---\n")
with open("story.txt") as f:
    content=f.read().split()

length=int(input("Enter Length of Words:"))

words=[]
for i in content:
    if(len(i)==length):
        words.append(i.lower())

words=set(words)
words=list(words)
words=sorted(words)
print(words)
