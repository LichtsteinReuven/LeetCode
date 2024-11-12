/*
You have a long flowerbed in which some of the plots are planted, and some are not.
However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty,
and an integer n, return true if n new flowers can be planted in the flowerbed without violating
the no-adjacent-flowers rule and false otherwise.


Example 1:
    Input: flowerbed = [1,0,0,0,1], n = 1
    Output: true

Example 2:
    Input: flowerbed = [1,0,0,0,1], n = 2
    Output: false

Constraints:
    1 <= flowerbed.length <= 2 * 10^4
    flowerbed[i] is 0 or 1.
    There are no two adjacent flowers in flowerbed.
    0 <= n <= flowerbed.length
*/

bool canPlaceFlowers(int* flowerbed, int flowerbedSize, int n)
{
    if (n == 0)
    {
        return true;
    }

    int number_of_optional_flowers = 0;

    // Begining of array only needs 2 consecetive zeros...
    int consecutive_zeros = 1;

    for (int i = 0; i < flowerbedSize; i++)
    {
        if (flowerbed[i] == 1)
        {
            consecutive_zeros = 0;
        }
        else
        {
            consecutive_zeros++;
            if (consecutive_zeros == 3)
            {
                number_of_optional_flowers++;
                consecutive_zeros = 1;

                if (number_of_optional_flowers == n)
                {
                    return true;
                }
            }
        }
    }

    if (consecutive_zeros == 2)
    {
        number_of_optional_flowers++;
    }

    return number_of_optional_flowers >= n;

}