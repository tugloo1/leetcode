from unittest import TestCase


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # First go through and see where the cost to get to the next station is
        possible_starting_points = set()
        num_of_stations = len(gas)
        for i, gas_available in enumerate(gas):
            # If the gas availabe is greater than the cost needed to get to the next station
            if gas_available >= cost[i]:
                possible_starting_points.add(i)

        for starting_point in list(possible_starting_points):
            current_gas = 0
            for i in self.get_wrap_index(starting_point, num_of_stations):
                if current_gas < 0:
                    break
                current_gas = current_gas + gas[i] - cost[i]
            if current_gas < 0:
                possible_starting_points.remove(starting_point)
        if len(possible_starting_points) == 1:
            return possible_starting_points.pop()
        else:
            return -1

    @staticmethod
    def get_wrap_index(s, length):
        starting = s
        while True:
            yield s
            s = (s + 1) % length
            if s == starting:
                return


class SolutionTest(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_can_complete_circuit(self):
        gas = [1, 2, 3, 4, 5]
        cost = [3, 4, 5, 1, 2]
        o = self.sol.canCompleteCircuit(gas, cost)
        self.assertEqual(o, 3)

    def test2(self):
        gas = [3, 3, 4]
        cost = [3, 4, 4]
        o = self.sol.canCompleteCircuit(gas, cost)
        self.assertEqual(o, -1)

    def test3(self):
        gas = [5, 1, 2, 3, 4]
        cost = [4, 4, 1, 5, 1]
        o = self.sol.canCompleteCircuit(gas, cost)
        self.assertEqual(o, 4)



