"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
    Input: "()"
    Output: true

Example 2:
    Input: "()[]{}"
    Output: true

Example 3:
    Input: "(]"
    Output: false

Example 4:
    Input: "([)]"
    Output: false

Constraints:
    - 1 <= s.length <= 10^4
    - s consists of parentheses only '()[]{}'.
"""

class Solution(object):
    OPEN_BRACKETS = ['(', '[', '{']
    BRACKETS_MAP = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        if len(s) % 2 != 0:
            return False
        for char in s:
            if char in self.OPEN_BRACKETS:
                stack.append(char)
            elif not stack:
                return False
            elif char != self.BRACKETS_MAP[stack.pop()]:
                return False
        return not stack

sol = Solution()
print(sol.isValid("()"))  # True
print(sol.isValid("()[]{}"))  # True
print(sol.isValid("(]"))  # False
print(sol.isValid("([)]"))  # False
print(sol.isValid("{[]}"))  # True
print(sol.isValid("["))  # False
print(sol.isValid("]"))  # False
print(sol.isValid("{{"))  # False
print(sol.isValid("{{}"))  # False
print(sol.isValid("{{}}"))  # True
print(sol.isValid(""))  # False