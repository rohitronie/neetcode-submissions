class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = defaultdict(int)
        for i, n in enumerate(nums):
            count[n] += 1
        
        freq = [[] for _ in range(len(nums) + 1)]
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in reversed(range(len(freq))):
            for e in freq[i]:
                res.append(e)
                if len(res) == k:
                    return res