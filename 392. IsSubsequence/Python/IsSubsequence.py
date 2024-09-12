"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters.
(ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
    Input: s = "abc", t = "ahbgdc"
    Output: true

Example 2:
    Input: s = "axc", t = "ahbgdc"
    Output: false

Constraints:
    0 <= s.length <= 100
    0 <= t.length <= 10^4
    s and t consist only of lowercase English letters.
"""


def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    s_length = len(s)
    t_length = len(t)
    if s_length == 0:
        return True
    if s_length > t_length:
        return False
    s_idx = t_idx = 0
    while t_idx < t_length:
        if s[s_idx] == t[t_idx]:
            s_idx += 1
        if s_idx == s_length:
            return True
        t_idx += 1
    return False
