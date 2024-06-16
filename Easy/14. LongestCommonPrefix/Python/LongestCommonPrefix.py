"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Constraints:
- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] consists of only lowercase English letters.
"""


def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    longest_prefix = ""

    # Iterate through the characters of the first string
    # and compare it with the characters of the other strings
    # at the same index.
    for i in range(len(strs[0])):
        for string in strs:
            # If the index is out of bounds or the character is not the same
            # as the character in the first string, return the previously found prefix.
            if len(string) <= i or string[i] != strs[0][i]:
                return longest_prefix
        # If all characters are the same, add the character to the prefix.
        longest_prefix += strs[0][i]
    return longest_prefix
