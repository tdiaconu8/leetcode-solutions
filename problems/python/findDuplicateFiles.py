from typing import List


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        groups, res = {}, []
        for path in paths:
            elems = path.split(' ')
            if len(elems) == 1:
                path, content = elems.split('(')
                groups[content[:-1]] = groups.get(content[:-1], []) + [path]
            else:
                for subPath in elems[1:]:
                    subRoot, content = subPath.split('(')
                    groups[content[:-1]] = groups.get(content[:-1], []) + [elems[0]+'/'+subRoot]
        
        for key, val in groups.items():
            if len(val) >= 2:
                res.append(val)
        
        return res