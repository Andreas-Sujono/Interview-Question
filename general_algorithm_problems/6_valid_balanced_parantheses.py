'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Note that an empty string is also considered valid.
'''

class Solution:
  def isValid(self, s):
    # Fill this in.
    stack = []
    if s == '':
        return True
    for i in s:
        if(i == ')'):
            if(len(stack) > 0 and stack[-1] == '('):
                stack.pop()
            else:
                return False
        elif(len(stack) > 0 and i == ']'):
            if(stack[-1] == '['):
                stack.pop()
            else:
                return False
        elif(len(stack) > 0 and i == '}'):
            if(stack[-1] == '{'):
                stack.pop()
            else:
                return False
        else:
            stack.append(i)
    
    return True if len(stack) == 0 else False

# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))