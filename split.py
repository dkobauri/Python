"""
TASK:
Your task is to write your own function, 
which behaves almost exactly like the original split() method, i.e.:
"""

def mysplit(strng):
    
    templist = []
    word = ""
    
    for ch in strng:
        if ch != " ":
            word += ch
        elif word:
            templist.append(word)
            word = ""
            
    if word:
        templist.append(word)
    
    return(templist)

print(mysplit("To be or not to be, that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
