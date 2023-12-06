#!/usr/bin/python3

def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if (roman_string is None or type(roman_string) != str):
        return (0)
    sum1 = 0
    sum2 = 0
    # Case: LXXXVII L(50) + X(10) + X(10) + x(10) + V(5) + I(1) + I(1)
    for char in roman_string:
        if roman[char] <= sum2:
            sum1 += roman[char]
        else:
            sum1 += roman[char] - (sum2 * 2)
        sum2 = roman[char]
    return sum1
