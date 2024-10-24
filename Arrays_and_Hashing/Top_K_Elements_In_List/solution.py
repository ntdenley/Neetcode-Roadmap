class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for n in nums:
            counts[n] += 1
        
        return [key for key, val in sorted(counts.items(), key=lambda item: item[1])][-k:]
        