from typing import List
from unittest import TestCase


class Solution():
    def generateParenthesis(self, n: int) -> List[str]:
        start, end = '(', ')'
        stack = [start]
        count_map = {start: 1, end: 0}
        output = []
        popped = False
        last_popped = None
        while stack:
            if popped:
                if last_popped == end:
                    last_popped = stack.pop()
                    popped = True
                    count_map[last_popped] -= 1
                    continue
                elif last_popped == start:
                    if count_map[end] < count_map[start]:
                        # Add the right tree
                        stack.append(end)
                        count_map[end] += 1
                    else:
                        last_popped = stack.pop()
                        popped = True
                        count_map[last_popped] -= 1
                        continue
            popped = False
            if count_map[start] < n:
                stack.append(start)
                count_map[start] += 1
            elif count_map[end] < n:
                stack.append(end)
                count_map[end] += 1
            else:
                # We've reached the end of tree
                output.append(''.join(stack))
                last_popped = stack.pop()
                popped = True
                count_map[last_popped] -= 1
        return output



class SolutionTest(TestCase):
    def tests(self):
        s = Solution()
        self.assertEqual(s.generateParenthesis(1), ['()'])
        self.assertEqual(s.generateParenthesis(2), ['(())', '()()'])
        self.assertEqual(s.generateParenthesis(3), ['((()))', '(()())', '(())()', '()(())', '()()()'])
