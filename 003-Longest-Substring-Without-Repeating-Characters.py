#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3.

Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''

class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s:str
        :rtype :int
        """
        ans = 0
        strLen = len(s)
        for i in range(strLen):
            for j in range(i+1, strLen+1):
                if self.allUnique(s, i, j):
                    ans = max(ans, j - i)
        return ans

    def allUnique(self, s, start, end):
        strs = set()
        for i in range(start, end):
            if s[i] in strs:
                return False
            else:
                strs.add(s[i])
        return True

if __name__ == '__main__':
    res = Solution().lengthOfLongestSubstring('p')
    print res