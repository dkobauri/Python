"""
TASK:

Your task is to write a program which answers the following question: 
- are the characters comprising the first string hidden inside the second string?
"""

str1 = "donor"
str2 = "Nabucodonosor"

lst = []
status = "Yes"

for ch in str2:
    lst.append(ch)
   
for chr in str1:
    if chr not in lst:
        status = "No"

print(status)