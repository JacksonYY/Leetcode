#!/usr/bin/env python
# -*- coding: utf-8 -*——

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        strDict = {}
        strLen = len(s)
        i, j, ans = 0, 0, 0
        while i < strLen and j < strLen:
            if strDict.has_key(s[j]):
                i = max(strDict[s[j]], i)
            ans = max(ans, j - i + 1)
            strDict[s[j]] = j + 1
            j += 1
        return ans