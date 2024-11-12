/*
Given an integer array nums, return true if there exists a triple of indices (i, j, k)
such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.


Example 1:
    Input: nums = [1,2,3,4,5]
    Output: true
    Explanation: Any triplet where i < j < k is valid.

Example 2:
    Input: nums = [5,4,3,2,1]
    Output: false
    Explanation: No triplet exists.

Example 3:
    Input: nums = [2,1,5,0,4,6]
    Output: true
    Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

Constraints:
    1 <= nums.length <= 5 * 10^5
    -23^1 <= nums[i] <= 231 - 1
*/

class Solution
{
public:
    bool increasingTriplet(vector<int>& nums)
    {
        if (nums.size() < 3)
        {
            return false;
        }

        int numsSize = nums.size();

        vector<int> minI(numsSize);
        minI[0] = nums[0];

        for (int i = 1; i < numsSize; i++)
        {
            minI[i] = min(minI[i -1 ], nums[i]);
        }

        vector<int> maxI(nums.size());
        maxI[nums.size() - 1] = nums[numsSize - 1];

        for (int i = numsSize - 2; i >= 0; i--)
        {
            maxI[i] = max(maxI[i + 1], nums[i]);
        }

        for (int i = 1; i < numsSize - 1; i++)
        {
            if (minI[i - 1] < nums[i] && nums[i] < maxI[i + 1])
            {
                return true;
            }
        }

        return false;
    }
};