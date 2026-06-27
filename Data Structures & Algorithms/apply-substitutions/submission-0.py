class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        map = {}
        for r in replacements:
            map[r[0]] = r[1]

        resolved = {}
        for key in map:
            self.resolve(key, map, resolved)

        parts = text.split("%")
        res = []
        for i in range(len(parts)):
            if i % 2 == 0:
                res.append(parts[i])
            else:
                res.append(resolved[parts[i]])
        return "".join(res)

    def resolve(self, key, map, resolved):
        if key in resolved:
            return resolved[key]

        val = map[key]
        if "%" not in val:
            resolved[key] = val
            return val

        parts = val.split("%")
        res = []
        for i in range(len(parts)):
            if i % 2 == 0:
                res.append(parts[i])
            else:
                res.append(self.resolve(parts[i], map, resolved))

        resolved[key] = "".join(res)
        return resolved[key]
