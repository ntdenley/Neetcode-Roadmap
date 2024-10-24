class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Create a dictionary of resulting anagrams
        res = defaultdict(list)

        # Iterate over all strings in the input list
        for s in strs:
            # Sort the string, since all anagrams will have the same sorted str
            sortedS = ''.join(sorted(s))

            # Add it based on the sorted string
            res[sortedS].append(s)
        
        # Return the values, or a list of the anagram lists!
        return res.values()