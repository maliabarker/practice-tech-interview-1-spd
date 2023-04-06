class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:
            nums.remove(val)
        return len(nums)

# The question is asking me to find all occurences of a given integer 
# value in a list of integers, remove these values, then return back 
# the number of elements in the list of integers that aren't equal to 
# the value of the integer to remove (aka the length of the list with 
# all occurences of the given integer removed)

# We assume the array of numbers is a list of integers and the array 
# does not have a set data structure. I am also coding this in python. 
# We can also assume that I can use python built in array functions like 
# len() and remove()

'''
Psuedocode:
    Iterate over the list of nums
        If the list of nums has val in it, remove.
    Return the length of the list with vals removed.
'''

# This would be O(n^2) because loop