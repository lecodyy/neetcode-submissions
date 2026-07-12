class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        
        heap = []
        for num, freq in hashmap.items():
            heapq.heappush(heap, (-freq, num))
        results = []
        for i in range(k):
            results.append(heapq.heappop(heap)[1])
        return results

