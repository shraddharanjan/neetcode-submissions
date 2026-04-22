class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-g for g in gifts]
        heapq.heapify(gifts)
        res = 0 

        while k > 0:
            gift = floor(sqrt(abs(heapq.heappop(gifts))))
            heapq.heappush(gifts, -gift)
            k -= 1
            
        for gift in gifts:
            res += abs(gift)

        return int(res)