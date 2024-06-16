"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together.
12 is written as XII, which is simply X + II.
The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is written as IV.
Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.

There are six instances where subtraction is used:
I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

Constraints:
- 1 <= s.length <= 15
- s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
- It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""


ROMAN_DICT = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def romanToInt(self, s):
    """
    :type s: str
    :rtype: int
    """
    # Base case: if s is empty, return 0
    if not s:
        return 0
    # Base case: if s has only one character, return the value of that character
    if len(s) == 1:
        return roman_dict[s]

    # If the value of the first character is less than the value of the second character,
    # subtract the first character from the second character
    # and call the function recursively with the rest of the string
    if roman_dict[s[0]] < roman_dict[s[1]]:
        return roman_dict[s[1]] - roman_dict[s[0]] + self.romanToInt(s[2:])

    # If the value of the first character is greater than or equal to the value of the second character,
    # add the value of the first character and call the function recursively with the rest of the string
    return roman_dict[s[0]] + self.romanToInt(s[1:])
