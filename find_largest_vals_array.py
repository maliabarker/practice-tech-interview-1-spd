'''
Given an array a of n numbers and a count k find the k largest values in the array a.
Example: a=[5, 1, 3, 6, 8, 2, 4, 7], k=3  ⇒  [6, 8, 7]
'''

# CLARIFYING QUESTIONS:
    # Can I use python built in methods like min(), max()

def find_k_largest_vals(arr, k):
    # array is array of numbers
    # k is amount of highest numbers you need to find

    # Instantiate array to keep return numbers in
    # Iterate through the list of numbers
        # If the index is less than k
            # Add the number to the return list
        # Else
            # If the number at the index is greater than the smallest value in the return list 
                # replace that value with the number

    # this would be O(n^3) time complexity because min() and index both iterate through the list, so there are three total iterations
    # can definitely improve on this

    return_arr = []
    for i in range(len(arr)):
        if i < k:
            return_arr.append(arr[i])
        else:
            if arr[i] > min(return_arr):
                return_arr[return_arr.index(min(return_arr))] = arr[i]
    return return_arr

    # simplest is to sort the array and then return from k to end
    # arr.sort(reverse=True)
    # return arr[:k]

    # the other way is to do minheap or maxheap


arr = [5, 1, 3, 6, 8, 2, 4, 7]
k = 3
print(find_k_largest_vals(arr, k))
