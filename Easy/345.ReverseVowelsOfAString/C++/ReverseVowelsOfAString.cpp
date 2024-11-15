/*
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.



Example 1:
    Input: s = "IceCreAm"
    Output: "AceCreIm"
    Explanation:
    The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:
    Input: s = "leetcode"
    Output: "leotcede"

Constraints:
    1 <= s.length <= 3 * 10^5
    s consist of printable ASCII characters.
*/

class Solution
{
public:
    string reverseVowels(string s)
    {
        set<char> vowels = {'A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u'};

        stack<char> stringVowels;

        for (char c: s)
        {
            if (vowels.find(c) != vowels.end())
            {
                stringVowels.push(c);
            }
        }

        for (int i = 0; i < s.length(); i++)
        {
            if (vowels.find(s[i]) != vowels.end())
            {
                s[i] = stringVowels.top();
                stringVowels.pop();
            }
        }

        return s;
    }
};