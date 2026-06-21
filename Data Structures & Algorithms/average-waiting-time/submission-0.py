class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        cur_time = customers[0][0]
        av_time = 0
        for arrival, time in customers:
            cur_time = max(cur_time, arrival) + time
            av_time += cur_time - arrival
        return av_time / len(customers)



