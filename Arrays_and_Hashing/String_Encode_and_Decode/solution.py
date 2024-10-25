class Solution:

    def encode(self, strs: List[str]) -> str:

        # Create an empty string
        newStr = ""
        for s in strs:
            # For each string, add its length, followed by a hashtag and the string itself.
            newStr += str(len(s)) + "#" + s
        # Output the string
        return newStr

    def decode(self, s: str) -> List[str]:
        # Create an empty result list
        result = []

        # Initialize a pointer (index) at the start of the str
        i = 0
        while i < len(s):
            # Create a second pointer
            j = i
            # Shift the right index pointer until reaching the hashtag
            while s[j] != '#':
                j += 1
            length = int(s[i:j]) # Length of upcoming string is the number between index pointers i and j
            i = j + 1 # Set left pointer to beginning of string
            j = i + length # Set right pointer to the end

            # Add the string between i and j
            result.append(s[i:j])

            # Shift i up to j, beginning the next string
            i = j

        # Output the resulting string
        return result