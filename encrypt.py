"""
TASK:
Your task is to write a program which:

- asks the user for one line of text to encrypt;
- asks the user for a shift value (an integer number from the range 1..25 
- note: you should force the user to enter a valid shift value (don't give up and don't let bad data fool you!)
- prints out the encoded text.
"""

text = input("Enter your message: ")
shift = input("Enter your shift value: ")
result = ''

if int(shift) > 0 and int(shift) < 26:
    for ch in text:
        
        if not ch.isalpha():
            result += ch
        elif ch.isalpha():
            code = ord(ch) + int(shift)
            if ch.isupper():
                if code > ord("Z"):
                    result += chr(ord("A") + (code - ord("Z") - 1))
                else:
                    result += chr(code)
            elif ch.islower():
                if code > ord("z"):
                    result += chr(ord("a") + (code - ord("z") - 1))
                else:
                    result += chr(code)
else:
    print("Shift value must be in range 1 - 25.")
print(result)