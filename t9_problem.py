'''
Given a string of digits 2 to 9 a user has pressed on an 
old T9 telephone keypad, return a list of all possible 
letter combinations they could have been trying to type.

EXAMPLE 1:
t9_letters("23") ⇒ ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
'''

"""
PSUEDOCODE/THOUGHT PROCESS:

My first though is that we need a way to keep track of the 
letters that are associated with each number. To make the 
lookup time for these letters constant, I would create a 
dictionary that stores keys as the numbers and values as 
a list of possible numbers.

From there, I would do the simple solution. 
For each number, I would want to grab the corresponding letter 
array and loop over that, so we'll have this crazy long sequence of lists to iterate over eseentially.
This would be O(n^n)
"""

num_letter_dict = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}

def t9_letters(nums):
    if len(nums) == 0:
        return ['']
    possible_combos = []
    for letter in num_letter_dict[nums[0]]:
        trailing_chars = t9_letters(nums[1:])
        for trailing_letter in trailing_chars:
            possible_combos.append(str(letter + trailing_letter))
    return possible_combos

print(t9_letters('4663'))

def t9_letters_kai_solution(keys, leading=''):
    values = []
    key_pressed = keys[0]
    for letter in num_letter_dict[key_pressed]:
        if (len(keys) == 1):
            values.append(leading + letter)
        else:
            values += t9_letters_kai_solution(keys[1:], leading + letter)
    return values

print(t9_letters_kai_solution('23'))