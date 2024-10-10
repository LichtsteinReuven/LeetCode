"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi]
represent the start and the end of the ith interval and intervals is sorted in ascending order by starti.
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals
still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.


Example 1:
    Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
    Output: [[1,5],[6,9]]

Example 2:
    Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    Output: [[1,2],[3,10],[12,16]]
    Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Constraints:
    0 <= intervals.length <= 10^4
    intervals[i].length == 2
    0 <= starti <= endi <= 10^5
    intervals is sorted by starti in ascending order.
    newInterval.length == 2
    0 <= start <= end <= 10^5
"""
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        length = len(intervals)
        position = self._find_position(intervals, newInterval, 0, length - 1)

        if position == length:
            intervals.append(newInterval)
            return intervals

        element = intervals[position]

        if element[1] < newInterval[0] or element[0] > newInterval[1]:
            intervals.insert(position, newInterval)
            return intervals

        temp = position

        while element[0] <= newInterval[1]:
            temp += 1
            if temp == length:
                break
            element = intervals[temp]

        intervals[position][0] = min(intervals[position][0], newInterval[0])
        intervals[position][1] = max(intervals[temp - 1][1], newInterval[1])

        del intervals[position + 1: temp]

        return intervals

    def _find_position(self, intervals, new_interval, start, end):
        if start > end:
            return start

        middle = (start + end) // 2
        element = intervals[middle]
        if element[0] <= new_interval[0] <= element[1]:
            return middle

        if element[0] < new_interval[0]:
            return self._find_position(intervals, new_interval, middle + 1, end)

        return self._find_position(intervals, new_interval, start, middle - 1)