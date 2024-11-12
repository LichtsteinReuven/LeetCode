/*
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the
elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.


Example 1:
    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]

Example 2:
    Input: nums = [-1,1,0,-3,3]
    Output: [0,0,9,0,0]

Constraints:
    2 <= nums.length <= 10^5
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
*/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* productExceptSelf(int* nums, int numsSize, int* returnSize) {

    int* prefix = malloc(sizeof(int) * numsSize);
    int* suffix = malloc(sizeof(int) * numsSize);
    int* product = malloc(sizeof(int) * numsSize);

    *returnSize = numsSize;

    int partialProduct = 1;

    for (int i = 0; i < numsSize; i++)
    {
        prefix[i] = partialProduct;
        partialProduct *= nums[i];
    }

    partialProduct = 1;
    for (int i = numsSize - 1; i > -1; i--)
    {
        suffix[i] = partialProduct;
        partialProduct *= nums[i];
    }

    for (int i = 0; i < numsSize; i++)
    {
        product[i] = prefix[i] * suffix[i];
    }

    free(prefix);
    free(suffix);
    return product;
}