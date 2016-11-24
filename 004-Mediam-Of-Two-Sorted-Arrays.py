#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

'''

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1) + len(nums2)
        if n % 2 == 1:
            return self.findKth(nums1, nums2, n/2 + 1)
        else:
            small = self.findKth(nums1, nums2, n/2)
            big = self.findKth(nums1, nums2, n/2 + 1)
            return (small+big) / 2.0

    def findKth(self, nums1, nums2, k):
        if len(nums1) == 0:
            return nums2[k-1]
        if len(nums2) == 0:
            return nums1[k-1]
        if k == 1:
            return min(nums1[0], nums2[0])
        a = nums1[k/2 - 1] if len(nums1) >= k/2 else None
        b = nums2[k/2 - 1] if len(nums2) >= k/2 else None
        if (a is not None and a < b) or b is None:
            return self.findKth(nums1[k/2:], nums2, k - k / 2)
        else:
            return self.findKth(nums1, nums2[k/2:], k - k / 2)

if __name__ == '__main__':
     res = Solution().findMedianSortedArrays([1,3], [2])
     print res