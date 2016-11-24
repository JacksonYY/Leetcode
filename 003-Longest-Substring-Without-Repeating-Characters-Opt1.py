#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        strLen = len(s)
        charSet = set()
        ans, i, j = 0, 0, 0
        while i < strLen and j <strLen:
            if s[j] not in charSet:
                charSet.add(s[j])
                j += 1
                ans = max(ans, j - i)
            else:
                charSet.remove(s[i])
                i += 1
        return ans

if __name__ == '__main__':
    result = Solution().lengthOfLongestSubstring('efbcabd')
    print result




