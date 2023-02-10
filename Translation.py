
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "Qq":
            translation = translation + "ქ"
        elif letter in "w":
            translation = translation + "წ"
        elif letter in "W":
            translation = translation + "ჭ"
        elif letter in "Ee":
            translation = translation + "ე"
        elif letter in "r":
            translation = translation + "რ"
        elif letter in "R":
            translation = translation + "ღ"
        elif letter in "t":
            translation = translation + "ტ"
        elif letter in "T":
            translation = translation + "თ"
        elif letter in "Yy":
            translation = translation + "ყ"
        elif letter in "Uu":
            translation = translation + "უ"
        elif letter in "Ii":
            translation = translation + "ი"
        elif letter in "Oo":
            translation = translation + "ო"
        elif letter in "Pp":
            translation = translation + "პ"
        elif letter in "Aa":
            translation = translation + "ა"
        elif letter in "s":
            translation = translation + "ს"
        elif letter in "S":
            translation = translation + "შ"
        elif letter in "Dd":
            translation = translation + "დ"
        elif letter in "Ff":
            translation = translation + "ფ"
        elif letter in "Gg":
            translation = translation + "გ"
        elif letter in "Hh":
            translation = translation + "ჰ"
        elif letter in "j":
            translation = translation + "ჯ"
        elif letter in "J":
            translation = translation + "ჟ"
        elif letter in "Kk":
            translation = translation + "კ"
        elif letter in "Ll":
            translation = translation + "ლ"
        elif letter in "z":
            translation = translation + "ზ"
        elif letter in "Z":
            translation = translation + "ძ"
        elif letter in "x":
            translation = translation + "ხ"
        elif letter in "X":
            translation = translation + "ძ"
        elif letter in "c":
            translation = translation + "ც"
        elif letter in "C":
            translation = translation + "ჩ"
        elif letter in "Vv":
            translation = translation + "ვ"
        elif letter in "Bb":
            translation = translation + "ბ"
        elif letter in "Nn":
            translation = translation + "ნ"
        elif letter in "Mm":
            translation = translation + "მ"
        else:
            translation = translation + letter
    return translation


a = 1

while a < 10:
    print(translate(input("Enter a Phrase: ")))
