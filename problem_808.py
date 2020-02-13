from unittest import TestCase

"""
Serve 100 ml of soup A and 0 ml of soup B
Serve 75 ml of soup A and 25 ml of soup B
Serve 50 ml of soup A and 50 ml of soup B
Serve 25 ml of soup A and 75 ml of soup B
"""


class Solution:
    @staticmethod
    def soupServings(n: int) -> float:
        if n/25 >= 500 or n == 1:
            return 1
        last_layer = {(n, n): 1}
        total_prob = 0
        while last_layer:
            new_layer = {}
            for soup_quantity in last_layer.keys():
                probability = last_layer[soup_quantity]
                soup_a, soup_b = soup_quantity
                subtractions = [(100, 0), (75, 25), (50, 50), (25, 75)]
                if soup_quantity == (0, 0):
                    continue
                for s in subtractions:
                    if s == (100, 0) and soup_a == 0:
                        continue
                    soup_a_subtraction, soup_b_subtraction = s
                    new_soup_a = max(0, soup_a - soup_a_subtraction)
                    new_soup_b = max(0, soup_b - soup_b_subtraction)
                    new_prob = .25*probability
                    new_soup_quantity = (new_soup_a, new_soup_b)
                    if soup_a > 0 and new_soup_a == 0:
                        # Soup A ran out first
                        if new_soup_b > 0:
                            total_prob += new_prob
                        # Both soups ran out together
                        elif soup_b > 0 and new_soup_b == 0:
                            total_prob += 0.5*new_prob
                            continue
                    if new_soup_quantity in new_layer:
                        new_layer[new_soup_quantity] += new_prob
                    else:
                        new_layer[new_soup_quantity] = new_prob
            last_layer = new_layer
        return total_prob


class SolutionTest(TestCase):
    def test_soup_servings(self):
        self.assertEqual(Solution.soupServings(50), 0.625)
        self.assertEqual(Solution.soupServings(660295675), 1)
