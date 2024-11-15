/*
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1.
If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.


Example 1:
    Input: word1 = "abc", word2 = "pqr"
    Output: "apbqcr"
    Explanation: The merged string will be merged as so:
    word1:  a   b   c
    word2:    p   q   r
    merged: a p b q c r

Example 2:
    Input: word1 = "ab", word2 = "pqrs"
    Output: "apbqrs"
    Explanation: Notice that as word2 is longer, "rs" is appended to the end.
    word1:  a   b
    word2:    p   q   r   s
    merged: a p b q   r   s

Example 3:
    Input: word1 = "abcd", word2 = "pq"
    Output: "apbqcd"
    Explanation: Notice that as word1 is longer, "cd" is appended to the end.
    word1:  a   b   c   d
    word2:    p   q
    merged: a p b q c   d

Constraints:
    1 <= word1.length, word2.length <= 100
    word1 and word2 consist of lowercase English letters.
*/

#include <string.h>

char * mergeAlternately(char * word1, char * word2){
    int word1_length = strlen(word1);
    int word2_length = strlen(word2);
    int i = 0;
    int j = 0;
    int k = 0;

    // Called responsible to release the memory...
    char* merged = malloc(word1_length + word2_length + 1);

    while (j < word1_length && k < word2_length)
    {
        merged[i++] = word1[j++];
        merged[i++] = word2[k++];
    }

    while (j < word1_length)
    {
        merged[i++] = word1[j++];
    }
    while (k < word2_length)
    {
        merged[i++] = word2[k++];
    }
    merged[i] = '\0';
    return merged;
}