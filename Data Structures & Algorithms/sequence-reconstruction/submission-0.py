class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        n = len(nums)
        in_degree = [0] * (n + 1)
        graph = [set() for _ in range(n + 1)]

        for seq in sequences:
            for i in range(1, len(seq)):
                if seq[i] not in graph[seq[i - 1]]:
                    graph[seq[i - 1]].add(seq[i])
                    in_degree[seq[i]] += 1

        queue = deque()
        for i in range(1, n + 1):
            if in_degree[i] == 0:
                queue.append(i)

        idx = 0
        while queue:
            if len(queue) > 1:
                return False
            curr = queue.popleft()
            if idx >= n or nums[idx] != curr:
                return False
            idx += 1
            for nxt in graph[curr]:
                in_degree[nxt] -= 1
                if in_degree[nxt] == 0:
                    queue.append(nxt)
        return idx == n
