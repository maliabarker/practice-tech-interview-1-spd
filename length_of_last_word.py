'''
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

EXAMPLES:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
'''

# assumption 1: string contains at least one word
# assumption 2: I can use python methods

def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """

    '''
    PSUEDOCODE
    Split the string
    Use max method 
    Instantiate state variable to keep of the largest word as ''
    Iterate over list
        If len(word) > len(variable), replace
    return len(state variable)
    '''

    word_arr = s.split()
    return(len(word_arr[-1]))

    # print(word_arr)
    # longest_word = ''
    # for word in word_arr:
    #     if len(word) > len(longest_word):
    #         longest_word = word
    # return len(longest_word)


str_1 = "Hello World"
print(lengthOfLastWord(str_1))

str_2 = "   fly me   to   the moon  "
print(lengthOfLastWord(str_2))