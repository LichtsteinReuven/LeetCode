"""
You are given a string, s, and a list of words, words, that are all of the same length.
A concatenated string is formed by concatenating each word in the list words together.
Return all starting indices of substring(s) in s that is a concatenated string of each word in words exactly
once and without any intervening characters.

You can return the answer in any order.

Example 1:
    Input: s = "barfoothefoobarman", words = ["foo","bar"]
    Output: [0,9]
    Explanation:
                The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a
                permutation of words.
                The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a
                permutation of words.

Example 2:
    Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
    Output: []
    Explanation:
                There are no substrings in s that are a concatenation of words.

Example 3:
    Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
    Output: [6,9,12]
    Explanation:
                The substring starting at 6 is "foobar". It is the concatenation of ["foo","bar","the"].
                The substring starting at 9 is "foobar". It is the concatenation of ["bar","foo","the"].
                The substring starting at 12 is "foobar". It is the concatenation of ["foo","bar","the"].

Constraints:
    1 <= s.length <= 10^4
    s consists of lower-case English letters.
    1 <= words.length <= 5000
    1 <= words[i].length <= 30
    words[i] consists of lower-case English letters.
"""


def findSubstring(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    word_len = len(words[0])
    perm_len = end_idx = word_len * len(words)
    start_idx = 0
    result = []
    s_len = len(s)
    words_count = {}

    # Trying to save time by counting the words in the list here instead of counting them in the loop below
    for word in words:
        words_count[word] = words.count(word)
    while start_idx < s_len:
        perm = s[start_idx: end_idx]
        if len(perm) < perm_len:
            break

        # Splitting the permutation into words of the same length
        split_perm = [perm[i:i+word_len] for i in range(0, perm_len, word_len)]

        # Checking if the permutation is a permutation of the words
        for word in words_count.keys():
            if split_perm.count(word) != words_count[word]:
                break
        else:
            result.append(start_idx)
        start_idx += 1
        end_idx += 1
    return result
