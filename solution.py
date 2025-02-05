from typing import List

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if sorted(list(s1)) != sorted(list(s2)):
            return False
        else:
            count = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    count += 1
                    if count > 2:
                        return False
                    
            if count == 1:
                return False
            else:
                return True