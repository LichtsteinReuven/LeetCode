/*
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.


Example 1:
    Input: nums1 = [1,2,3], nums2 = [2,4,6]
    Output: [[1,3],[4,6]]
    Explanation:
    For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
    For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].

Example 2:
    Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
    Output: [[3],[]]
    Explanation:
    For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
    Every integer in nums2 is present in nums1. Therefore, answer[1] = [].

Constraints:
    1 <= nums1.length, nums2.length <= 1000
    -1000 <= nums1[i], nums2[i] <= 1000
*/

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** findDifference(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize, int** returnColumnSizes)
{
    int* numsIn1NotIn2 = malloc(nums1Size * sizeof(int));
    int numsIn1NotIn2Ctr = 0;

    for (int i = 0; i < nums1Size; i++)
    {
        bool found = false;

        for (int j = 0; j < nums2Size; j++)
        {
            if (nums1[i] == nums2[j])
            {
                found = true;
                break;
            }
        }

        if (!found)
        {
            bool alreadyIn = false;
            for (int k = 0; k < numsIn1NotIn2Ctr; k++)
            {
                if (numsIn1NotIn2[k] == nums1[i])
                {
                    alreadyIn = true;
                    break;
                }
            }
            if (!alreadyIn)
            {
                numsIn1NotIn2[numsIn1NotIn2Ctr++] = nums1[i];
            }
        }

    }

    int* firstArray = realloc(numsIn1NotIn2, numsIn1NotIn2Ctr * sizeof(int));

    int* numsIn2NotIn1 = malloc(nums2Size * sizeof(int));
    int numsIn2NotIn1Ctr = 0;

    for (int i = 0; i < nums2Size; i++)
    {
        bool found = false;

        for (int j = 0; j < nums1Size; j++)
        {
            if (nums2[i] == nums1[j])
            {
                found = true;
                break;
            }
        }

        if (!found)
        {
            bool alreadyIn = false;
            for (int k = 0; k < numsIn2NotIn1Ctr; k++)
            {
                if (numsIn2NotIn1[k] == nums2[i])
                {
                    alreadyIn = true;
                    break;
                }
            }
            if (!alreadyIn)
            {
                numsIn2NotIn1[numsIn2NotIn1Ctr++] = nums2[i];
            }
        }

    }

    int* secondArray = realloc(numsIn2NotIn1, numsIn2NotIn1Ctr * sizeof(int));

    int** returnArray = malloc(2 * sizeof(int*));
    returnArray[0] = firstArray;
    returnArray[1] = secondArray;

    int* sizes = malloc(2 * sizeof(int));
    sizes[0] = numsIn1NotIn2Ctr;
    sizes[1] = numsIn2NotIn1Ctr;

    *returnSize = 2;

    *returnColumnSizes = sizes;

    return returnArray;
}