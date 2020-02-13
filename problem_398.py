import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        selected_index = None
        count_seen = 0
        for i, num in enumerate(self.nums):
            if num == target:
                if selected_index == None:
                    selected_index = i
                    count_seen += 1
                else:
                    rand_int = random.randint(0, count_seen)
                    if rand_int == 0:
                        selected_index = i
                    count_seen += 1
        return selected_index
