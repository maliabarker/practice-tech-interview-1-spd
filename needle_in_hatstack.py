"""
Given two strings needle and haystack, return the index of 
the first occurrence of needle in haystack, or -1 if needle 
is not part of haystack.

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Instantiate i = 0
Iterate over each letter in the haystack string

"""

def strStr(self, haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    i = 0
    j = 0
    for char in haystack:
        if char == needle[j]:
            # keep going, increment j

            pass
            return i
        else:
            i += 1