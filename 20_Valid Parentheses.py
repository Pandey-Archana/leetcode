# https://leetcode.com/problems/valid-parentheses/

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    char_dict = {
        ')':'(',
        '}':'{',
        ']':'[',
    }
    input_stack = []
    input_stack = []
    for i in range(len(s)):
        if input_stack and s[i] in char_dict and input_stack[-1] == char_dict[s[i]]:
            input_stack.pop()
        else:
            input_stack.append(s[i])
    return(not bool(input_stack))

print(isValid("([)]"))