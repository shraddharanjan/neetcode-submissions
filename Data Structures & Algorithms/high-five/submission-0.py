class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        K = 5
        all_scores = defaultdict(list)  # Using defaultdict with list for min heap

        for item in items:
            student_id = item[0]
            score = item[1]

            heapq.heappush(all_scores[student_id], score)

            if len(all_scores[student_id]) > K:
                heapq.heappop(all_scores[student_id])

        solution = []
        for student_id in sorted(all_scores.keys()):
            total = sum(all_scores[student_id])
            solution.append([student_id, total // K])

        return solution