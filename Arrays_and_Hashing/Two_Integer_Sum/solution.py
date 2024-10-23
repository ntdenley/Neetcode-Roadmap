class Solution:
    # Two pointer approach
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Use a dictionary to keep track of past values/indices seen.
        past_indices = {}

        # Enumerate the nums list, since we want the indices
        for i, n in enumerate(nums):

            # Find the diff between target and current value
            diff = target - n

            # Check if we've seen the diff earlier in the list
            if diff in past_indices:
                # We have, return its index and the current one!
                return [past_indices[diff], i]

            # Not yet, let's record the current value/index though.
            past_indices[n] = i