/*
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
ans[i] is the number of 1's in the binary representation of i.


Example 1:
    Input: n = 2
    Output: [0,1,1]
    Explanation:
    0 --> 0
    1 --> 1
    2 --> 10

Example 2:
    Input: n = 5
    Output: [0,1,1,2,1,2]
    Explanation:
    0 --> 0
    1 --> 1
    2 --> 10
    3 --> 11
    4 --> 100
    5 --> 101

Constraints:
    0 <= n <= 10^5
*/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countBits(int n, int* returnSize) {
    int* numOfBits = malloc((n + 1) * sizeof(int));
    numOfBits[0] = 0;

    if (n > 0)
    {
        numOfBits[1] = 1;
    }

    int nextPower = 2;
    int innerCounter = 0;
    for (int i = 2; i <= n; i++)
    {
        if (i == nextPower)
        {
            nextPower *= 2;
            innerCounter = 0;
        }

        numOfBits[i] = 1 + numOfBits[innerCounter++];
    }

    *returnSize = n + 1;

    return numOfBits;
}