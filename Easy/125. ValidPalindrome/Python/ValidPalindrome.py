"""
A phrase is a palindrome if after converting all uppercase letters to lowercase letters and removing all
non-alphanumeric characters, the phrase reads the same forwards and backwards. Alphanumeric characters
are letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.

Example 3:
    Input: s = " "
    Output: false
    Explanation: s is an empty string "" after removing non-alphanumeric characters.
                 Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
    1 <= s.length <= 2 * 10^5
    s consists only of printable ASCII characters.
"""


def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    front = 0
    back = -1
    length = len(s)

    while front + (-back) < length:
        if not s[front].isalnum():
            front += 1
            continue
        if not s[back].isalnum():
            back -= 1
            continue
        if s[front].lower() != s[back].lower():
            return False
        else:
            front += 1
            back -= 1
    return True
