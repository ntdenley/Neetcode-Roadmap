class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # store all unique numbers in a set
        unique_nums = set(nums)

        # max sequence starts at 0 (in case of empty list)
        maxSeq = 0
        for num in nums:
            # nothing 1 less than current num, meaning new sequence
            if num-1 not in unique_nums:
                seq = 1
                # Increment the sequence so long as it continues in the set
                while(num+seq in unique_nums):
                    seq += 1
                # new record? set it!
                if seq > maxSeq:
                    maxSeq = seq
        # return the longest sequence
        return maxSeq
