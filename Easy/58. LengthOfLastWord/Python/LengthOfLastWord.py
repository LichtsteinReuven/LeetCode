"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word in the string.

A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: "  fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

Constraints:
1 <= s.length <= 10^4
s consists of only English letters and spaces ' '.
There will be at least one word in s.
"""


def lengthOfLastWord(self, s):
    """
    :type s: str
    :rtype: int
    """
    # strip() removes leading and trailing whitespaces
    # split() splits the string into a list of words separated by whitespaces
    # [-1] returns the last word in the list
    # len() returns the length of the last word
    return len(s.strip().split(' ')[-1])
