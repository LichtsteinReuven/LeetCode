/*
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some
(can be none) of the characters without disturbing the relative positions of the remaining characters.
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).


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
*/

bool isSubsequence(char* s, char* t) {
    int sLength = strlen(s);
    int tLength = strlen(t);

    if (sLength > tLength)
    {
        return false;
    }

    if (sLength == 0)
    {
        return true;
    }

    int sIdx = 0;

    for (int i = 0; i < tLength; i++)
    {
        if (s[sIdx] == t[i])
        {
            sIdx++;
            if (sIdx == sLength)
            {
                return true;
            }
        }
    }
    return false;
}