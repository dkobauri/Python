"""
TASK:
Your task is to write a program which:

- reads 9 rows of the Sudoku, each containing 9 digits (check carefully if the data entered are valid)
- outputs Yes if the Sudoku is valid, and No otherwise.
"""

sudoku = ["295743861", 
"431865927", 
"876192543", 
"387459216", 
"612387495", 
"549216738", 
"763524189", 
"928671354", 
"154938672"]

lst = []
unique = []
status = "Yes"

def checkForSpecificNumbers(str):
    result1 = "123456789"
    result2 = sorted(str)
    result3 = "".join(result2)
    if result1 == result3:
        return True 
    else: 
        return False

def uniqueNumberCheck(str):
	if len(str) == 9:
		try:
			num = int(str)
			return True
		except:
			return False
	else:
		return False

def checkUnique(str):
    for i in range(len(str)):
        for j in range(i + 1,len(str)):
            if(str[i] == str[j]):
                return False
    return True

# check rows

for row in sudoku:
    if (uniqueNumberCheck(row) and checkForSpecificNumbers(row) and checkUnique(row)):
        status = "Yes"
    else:
        status = "No"
        break

# check columns
    
for i in range(9):
    for j in range(9):
        lst.append(sudoku[j][i])
    str = "".join(lst)
    if (uniqueNumberCheck(str) and checkForSpecificNumbers(str) and checkUnique(str)):
        status = "Yes"
        lst = []
    else:
        status = "No"
        break

# check square 1

for i in range(0, 3):
    for j in range(0, 3):
        lst.append(sudoku[j][i])
str= "".join(lst)
if (uniqueNumberCheck(str) and checkForSpecificNumbers(str) and checkUnique(str)):
    status = "Yes"
    lst = []
else:
    status = "No"

# check square 2

for i in range(0, 3):
    for j in range(3, 6):
        lst.append(sudoku[j][i])
str= "".join(lst)
if (uniqueNumberCheck(str) and checkForSpecificNumbers(str) and checkUnique(str)):
    status = "Yes"
    lst = []
else:
    status = "No"

# check square 3

for i in range(0, 3):
    for j in range(6, 9):
        lst.append(sudoku[j][i])
str= "".join(lst)
if (uniqueNumberCheck(str) and checkForSpecificNumbers(str) and checkUnique(str)):
    status = "Yes"
    lst = []
else:
    status = "No"

# check square 4

for i in range(3, 6):
    for j in range(0, 3):
        lst.append(sudoku[j][i])
str= "".join(lst)
if (uniqueNumberCheck(str) and checkForSpecificNumbers(str) and checkUnique(str)):
    status = "Yes"
    lst = []
else:
    status = "No"
    
# check square 5

for i in range(3, 6):
    for j in range(3, 6):
        lst.append(sudoku[j][i])
str= "".join(lst)
if (uniqueNumberCheck(str) and checkForSpecificNumbers(str) and checkUnique(str)):
    status = "Yes"
    lst = []
else:
    status = "No"

# check square 6

for i in range(3, 6):
    for j in range(6, 9):
        lst.append(sudoku[j][i])
str= "".join(lst)
if (uniqueNumberCheck(str) and checkForSpecificNumbers(str) and checkUnique(str)):
    status = "Yes"
    lst = []
else:
    status = "No"
   
# check square 7

for i in range(6, 9):
    for j in range(0, 3):
        lst.append(sudoku[j][i])
str= "".join(lst)
if (uniqueNumberCheck(str) and checkForSpecificNumbers(str) and checkUnique(str)):
    status = "Yes"
    lst = []
else:
    status = "No"

# check square 8

for i in range(6, 9):
    for j in range(3, 6):
        lst.append(sudoku[j][i])
str= "".join(lst)
if (uniqueNumberCheck(str) and checkForSpecificNumbers(str) and checkUnique(str)):
    status = "Yes"
    lst = []
else:
    status = "No"

# check square 9

for i in range(6, 9):
    for j in range(6, 9):
        lst.append(sudoku[j][i])
str= "".join(lst)
if (uniqueNumberCheck(str) and checkForSpecificNumbers(str) and checkUnique(str)):
    status = "Yes"
    lst = []
else:
    status = "No"

print(status)