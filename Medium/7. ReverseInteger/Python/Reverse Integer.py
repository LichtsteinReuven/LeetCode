from ctypes import c_int32

"""
Given a 32-bit signed integer, reverse digits of an integer.
If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], 
then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
    Input: 123
    Output: 321
    
Example 2:
    Input: -123
    Output: -321
    
Example 3:
    Input: 120
    Output: 21
    
Constraints:
    -2^31 <= x <= 2^31 - 1            
"""


def reverse(self, x):
    """
    :type x: int
    :rtype: int
    """
    # Save the sign of the number
    sign = x < 0
    x = abs(x)
    # Create a 32-bit signed integer, doing it to emulate the 32-bit signed integer range
    reversed_x = c_int32(0)
    while x > 0:
        # Check if the number is out of the 32-bit signed integer range
        # If it is, return 0
        # Doing this checks in a jumps of 2, because the number is multiplied by 10
        # and that can make it be positive back again despite being out of the range
        # So, we need to check if the number is out of the range in the middle of the multiplication
        for i in range(2, 11, 2):
            num = c_int32(reversed_x.value * i)
            if num.value < 0:
                return 0
        reversed_x.value *= 10
        reversed_x.value += x % 10
        x = x // 10
    if sign:
        return -reversed_x.value
    return reversed_x.value
