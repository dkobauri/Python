"""
TASK:
Your task is to write a program which:

- asks the user for some text;
- checks whether the entered text is a palindrome, and prints result.

Note:
- assume that an empty string isn't a palindrome;
- treat upper- and lower-case letters as equal;
- spaces are not taken into account during the check - treat them as non-existent;
- there are more than a few correct solutions - try to find more than one.
"""

text = input("Enter your text: ")

result1 = ''
result2 = ''

for ch in text:
    if ch == " ":
        continue
    else:
        result1 += ch

result2 = "".join(reversed(result1))

if result1.lower() == result2.lower():
    print("It's a palindrome")
elif result1.lower() != result2.lower():
    print("It's not a palindrome")