from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost or len(cost) == 1:
            return 0
        cost.append(0)
        min_costs = [cost[0], cost[1]]

        if len(cost) == 2:
            return min(min_costs)

        for i in range(2, len(cost)):
            current_step_cost = cost[i]
            two_step_cost = min_costs[i - 2] + current_step_cost
            one_step_cost = min_costs[i - 1] + current_step_cost
            min_costs.append(min(one_step_cost, two_step_cost))
        return min_costs[-1]

