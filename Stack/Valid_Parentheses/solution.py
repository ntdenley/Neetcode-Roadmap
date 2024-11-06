class Solution:
    def isValid(self, s: str) -> bool:
        # Dictionary of complimenting brackets
        compliment = {')':'(', '}':'{', ']':'['}

        # Create a stack
        stack = []
        for c in s:
            # Begin a new "encapsulation", push the left bracket
            if c in "({[":
                stack.append(c)

            # End an "encapsulation", if we cant, it's not valid
            else:
                if len(stack) > 0 and stack[-1] == compliment[c]:
                    stack.pop() # Valid, remove the left bracket
                else:
                    return False # Invalid, return false

        # If we have open left brackets (i.e. stack size isn't zero),
        # the string is invalid.
        return len(stack) == 0
                
        