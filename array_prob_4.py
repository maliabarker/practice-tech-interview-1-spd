"""
Given two arrays a and b of numbers and a target value t, find a number from each array whose sum is closest to t.
Example: 
    a=[9, 13, 1, 8, 12, 4, 0, 5]
    b=[3, 17, 4, 14, 6]
    t=20  
    ⇒  [13, 6] or [4, 17] or [5, 14]
"""

"""
PSUEDOCODE:
Restate: We are finding pairs (one from array one, one from array two) of numbers that have sums close to t
Assumptions:
    We are returning an array of two numbers (integers)
    From the example we are given, it doesn't matter if the 'error' is higher or lower just same error (example +/- 1)

I think brute force would be to iterate over both and find all possible pairs, keep a running 'best match' variable to compare to, and keep track of the best matched numbers
I'm going to assume the time complexity of this will be O(n^2) because we would be doing a for loop in a for loop, so this is not ideal and can definitely be improved on
I would implement it like this:
Instantiate best_match_diff and best_match_nums
For each number in array1
    For each number is array 2
        Take the sum of the two numbers
        Get the absolute value of val from subtracting sum and t
        If this resulting difference is less than the current best_match_diff (or none, meaning it's the first one to compare)
            Make best_match_diff equal to this difference
            Make best match sum equal to an array of number 1 and 2
Return final best_match_sum array

Can improve this by using binary search on second array, this would be complexity of nlog(n)
"""

def closest_sum_arrays(arr1, arr2, t):
    # Can set infinity by using float('inf')
    # best_match_diff = float('inf')
    best_match_diff = None
    best_match_sum = None
    for num1 in arr1:
        for num2 in arr2:
            num_sum = num1 + num2
            diff = abs(num_sum - t)
            print('NUMS:', [num1, num2], 'SUM:', num_sum, 'DIFF:', diff)
            if best_match_diff == None or diff < best_match_diff:
                print('BEST MATCH FOUND')
                best_match_diff = diff
                best_match_sum = [num1, num2]
    print('FINAL', best_match_sum)
    return best_match_sum


a=[9, 13, 1, 8, 12, 4, 0, 5]
b=[3, 17, 4, 14, 6]
t=20
closest_sum_arrays(a, b, t)