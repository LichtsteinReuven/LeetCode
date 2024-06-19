"""
Given a string s, find the length of the longest substring
without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence
and not a substring.

Example 4:
Input: s = ""
Output: 0

Constraints:
0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.
"""

def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    max_length = 0
    substring = ""
    for char in s:
        if char in substring:
            # Update max_length if the current substring is longer
            if len(substring) > max_length:
                max_length = len(substring)
            # Find the index of the first occurrence of the character in the substring
            # and slice the substring from that index to the end
            substring = substring[substring.find(char)+1:]
        substring += char
    # Update max_length if the current substring is longer
    if len(substring) > max_length:
        return len(substring)
    return max_length
