weight = input("Weight: ")
unit = input("(L)bs or (K)g: ")

if unit.upper() == "K":  # same as unit == "K" or unit == "k":
    Lbs = float(weight) * 2.20462262
    print(f"{str(weight)} Kg is equal to {str(round(Lbs,2))} Lbs.")
elif unit.upper() == "L":  # same as unit == "L" or unit == "l":
    Kg = float(weight) * 0.45359237
    print(f"{str(weight)} Lbs is equal to {str(round(Kg,2))} Kg.")
else:
    print("Please Indicate Correct Unit!")
