"""
TASK:
Your task is to write a program which:

- asks the user for two separate texts;
- checks whether, the entered texts are anagrams and prints the result.

Note:
- assume that two empty strings are not anagrams;
- treat upper- and lower-case letters as equal;
- spaces are not taken into account during the check - treat them as non-existent
"""

text1 = input("Enter your first text: ")
text2 = input("Enter your second text: ")

result1 = []
result2 = []


for ch in text1:
    if ch == " ":
        continue
    else:
        result1.append(ch.lower())
        
for ch in text2:
    if ch == " ":
        continue
    else:
        result2.append(ch.lower())

result1 = sorted(result1)
result2 = sorted(result2)

if result1 == result2:
    print("Anagrams")
else: 
    print("Not anagrams")