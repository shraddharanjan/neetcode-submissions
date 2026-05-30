class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        map_dict = {}
        for i in range(len(ppid)):
            if ppid[i] > 0:
                if ppid[i] not in map_dict:
                    map_dict[ppid[i]] = []
                map_dict[ppid[i]].append(pid[i])

        result = [kill]
        self.getAllChildren(map_dict, result, kill)
        return result

    def getAllChildren(self, map_dict, result, kill):
        if kill in map_dict:
            for child_id in map_dict[kill]:
                result.append(child_id)
                self.getAllChildren(map_dict, result, child_id)