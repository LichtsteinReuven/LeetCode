"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"

Constraints:
1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""


def convert(self, s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if not s:
        return ""
    if numRows == 1 or len(s) <= numRows:
        return s
    rows = [""] * numRows
    i = 0
    rows[i] += s[i]
    while i < len(s):
        # Go one by one to the next row until the last row
        # and then go one by one to the previous row until the first row (2nd range)
        for j in range(1, numRows):
            i += 1
            if i >= len(s):
                break
            rows[j % numRows] += s[i]
        for j in range(numRows - 2, -1, -1):
            i += 1
            if i >= len(s):
                break
            rows[j % numRows] += s[i]
    return "".join(rows)
