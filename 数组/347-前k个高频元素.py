class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []
        hash_map = dict()
        for n in nums:
            hash_map.setdefault(n, 0)
            hash_map[n] += 1

        sort_dict = dict(sorted(hash_map.items(), key=lambda x: x[1], reverse=True)[:k])
        return list(sort_dict.keys())