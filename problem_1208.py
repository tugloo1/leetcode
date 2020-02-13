from unittest import TestCase


class Solution:
    @staticmethod
    def equal_substring(s: str, t: str, max_cost: int) -> int:
        i = 0
        j = 0
        max_len = len(s)
        max_seen_len_substring = 0
        window_cost = abs(ord(s[i]) - ord(t[i]))  #starting window cost
        while i < max_len and j < max_len:
            if i > j:
                j = i
                window_cost = abs(ord(s[i]) - ord(t[i]))
                continue

            if window_cost <= max_cost:
                window_size = j - i + 1
                max_seen_len_substring = max(window_size, max_seen_len_substring)
                j += 1
                if not j < max_len:
                    break
                jth_cost = abs(ord(s[j]) - ord(t[j]))
                window_cost += jth_cost
            else:
                ith_cost = abs(ord(s[i]) - ord(t[i]))
                window_cost -= ith_cost
                i += 1

            if i == j and j + 1 < max_len:
                j += 1
                ith_cost = abs(ord(s[i]) - ord(t[i]))
                jth_cost = abs(ord(s[j]) - ord(t[j]))
                window_cost = ith_cost + jth_cost
        return max_seen_len_substring


class SolutionTest(TestCase):
    def test(self):
        self.assertEqual(Solution.equal_substring('a', 'b', 2), 1)
        self.assertEqual(Solution.equal_substring('ab', 'ad', 0), 1)
        self.assertEqual(Solution.equal_substring('abcd', 'bcdf', 3), 3)
        self.assertEqual(Solution.equal_substring('krrgw', 'zjxss', 19), 2)
        self.assertEqual(Solution.equal_substring('abcd', 'cdef', 3), 1)
        self.assertEqual(Solution.equal_substring('abcd', 'cdef', 1), 0)
        self.assertEqual(Solution.equal_substring('abcd', 'acde', 0), 1)
        self.assertEqual(Solution.equal_substring("npzdfy", "xmsgby", 14), 4)
        self.assertEqual(Solution.equal_substring("krpgjbjjznpzdfy", "nxargkbydxmsgby", 14), 4)
        self.assertEqual(Solution.equal_substring('anryddgaqpjdw', 'zjhotgdlmadcf', 5), 1)
