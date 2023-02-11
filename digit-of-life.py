"""
TASK:
Your task is to write a program which:

- asks the user her/his birthday (in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY - actually, the order of the digits doesn't matter)
- outputs the Digit of Life for the date.
"""

birthday  = input("Enter you birthday date in the following format YYYYMMDD or YYYYDDMM: ")

lst = []
total = 0

for x in birthday:
    lst.append(int(x))
  
total = sum(lst)

if total > 9:
    total = int(total / 10) + (total % 10)

print(total)