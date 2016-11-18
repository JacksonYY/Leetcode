
# Time O(n^2)
# Space O(1)

# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.
# You may assume that each input would have exactly one solution.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


class Solution(object):
    '''
    add up to a specific target
    '''
    def twosum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numslen = len(nums)
        for i in range(numslen):
            for k in range(i+1, numslen):
                if nums[i] + nums[k] == target:
                    return [i, k]

if __name__ == '__main__':
    RESULT = Solution().twosum([3, 2, 4], 6)
    print RESULT
