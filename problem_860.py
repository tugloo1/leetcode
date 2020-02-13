from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        register = {5: 0, 10: 0, 20: 0}
        for b in bills:
            register[b] += 1
            if b == 5:
                continue
            elif b == 10 and register[5] >= 1:
                register[5] -= 1
            elif b == 20 and register[5] >= 1 and register[10] >= 1:
                register[5] -= 1
                register[10] -= 1
            elif b == 20 and register[5] >= 3:
                register[5] -= 3
            else:
                return False
        return True
