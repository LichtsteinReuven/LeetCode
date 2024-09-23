"""
Given two binary strings a and b, return their sum as a binary string.


Example 1:
    Input: a = "11", b = "1"
    Output: "100"

Example 2:
    Input: a = "1010", b = "1011"
    Output: "10101"

Constraints:
    1 <= a.length, b.length <= 10^4
    a and b consist only of '0' or '1' characters.
    Each string does not contain leading zeros except for the zero itself.
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = carry = 0
        len_a, len_b = len(a), len(b)
        length = max(len_a, len_b)
        a = a[::-1]
        b = b[::-1]
        res = ""
        while i < length:
            sum_ = carry
            if i < len_a:
                sum_ += int(a[i])
            if i < len_b:
                sum_ += int(b[i])
            if sum_ > 1:
                carry = 1
                sum_ %= 2
            else:
                carry = 0
            res += str(sum_)
            i += 1
        if carry:
            res += "1"
        return res[::-1]

sol = Solution()
print(sol.addBinary("11", "1"))  # "100"