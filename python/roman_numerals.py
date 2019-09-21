'''
This problem was asked by Facebook.

Given a number in Roman Numeral format, convert it to decimal.
The values of Roman numerals are as follows:
{
    'M' : 1000,
    'D' : 500,
    'C' : 100,
    'L' : 50,
    'X' : 10,
    'V' : 5,
    'I' : 1
}
In addition, note that the Roman numeral system uss subtractive notation
 for numbers such as IV and XL.
For instance, for the input XIV, return 14.
'''

def convert_to_decimal(roman_numeral):
    roman_map = {
            'M' : 1000,
            'D' : 500,
            'C' : 100,
            'L' : 50,
            'X' : 10,
            'V' : 5,
            'I' : 1
            }
    decimal = 0
    index = 0
    while index < len(roman_numeral):
        current_numeral = roman_map[roman_numeral[index]]
        if index == len(roman_numeral) - 1:
            decimal += current_numeral
            break
        next_numeral = roman_map[roman_numeral[index+1]]
        if current_numeral < next_numeral:
            decimal += (next_numeral - current_numeral)
            index += 2
        else:
            decimal += current_numeral
            index += 1
    return decimal

if __name__ == '__main__':
    roman_numerals = ['IV', 'XL', 'CXIV', 'XVIII']
    for roman_numeral in roman_numerals:
        print(convert_to_decimal(roman_numeral))
