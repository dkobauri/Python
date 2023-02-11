"""
TASK:
Your task is to write a program which is able to simulate the work of a seven-display device, 
although you're going to use single LEDs instead of segments.
"""

nums = {
    '0': ['###', '# #', '# #', '# #', '###'],
    '1': ['  #', '  #', '  #', '  #', '  #'],
    '2': ['###', '  #', '###', '#  ', '###'],
    '3': ['###', '  #', '###', '  #', '###'],
    '4': ['# #', '# #', '###', '  #', '  #'],
    '5': ['###', '#  ', '###', '  #', '###'],
    '6': ['###', '#  ', '###', '# #', '###'],
    '7': ['###', '  #', '  #', '  #', '  #'],
    '8': ['###', '# #', '###', '# #', '###'],
    '9': ['###', '# #', '###', '  #', '###'],
}

value = input("Enter only numbers: ")

try:
    digits = [nums[num] for num in value]
    for i in range(5):
        print(" ".join(number[i] for number in digits))
except KeyError:
    print("ONLY NUMBERS!")