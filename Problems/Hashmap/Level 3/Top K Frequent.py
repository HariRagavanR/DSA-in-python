import heapq
nums = [1,1,1,2,2,3]
k = 2
def top_k_freq(nums,k):
    freq = {}

    for num in nums:
        freq[num] = freq.get(num,0) + 1

    heap = []

    for num, freq in freq.items():
        heapq.heappush(heap,(freq,num))

        if len(heap) > k:
            heapq.heappop(heap)

    return [num for freq, num in heap]

print(top_k_freq(nums,k))

