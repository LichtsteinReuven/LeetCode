DECIMAL_BASE = 10


# A solution without converting the integer to string
def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False
    reversed_x = 0
    original_x = x
    while x > 0:
        reversed_x = reversed_x * DECIMAL_BASE + x % DECIMAL_BASE
        x = x // DECIMAL_BASE
    return original_x == reversed_x