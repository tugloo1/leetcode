from typing import List
import heapq

class Node(object):
    def __init__(self, node, edge_weight):
        self.node = node
        self.edge_weight = edge_weight

    def __repr__(self):
        return f'Node: {self.node} Edge Weight: {self.edge_weight}'

    def __lt__(self, other):
        return self.edge_weight < other.edge_weight



class Solution:
    @staticmethod
    def manhatten_dist(point1: List[int], point2: List[int]):
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        total_cost = 0
        num_of_nodes = len(points)
        nodes = {0} # Just picking the first node
        heap = []
        for i, point in enumerate(points):
            if i in nodes:
                continue
            heap_node = Node(i, self.manhatten_dist(points[0], point))
            heap.append(heap_node)
        heapq.heapify(heap)
        print(heap)
        while len(nodes) < num_of_nodes:
            frontier_node = heapq.heappop(heap)
            print('Popped ' + str(frontier_node))
            if frontier_node.node in nodes:
                print('Skipping')
                continue
            nodes.add(frontier_node.node)
            total_cost += frontier_node.edge_weight
            # Add the next frontier
            for i, point in enumerate(points):
                if i in nodes:
                    continue
                heap_node = Node(i, self.manhatten_dist(points[frontier_node.node], point))
                heapq.heappush(heap, heap_node)



        print('Total Cost ' + str(total_cost))
        return total_cost


s = Solution()
# case1 = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# o1 = 20


# assert s.minCostConnectPoints(case1) == o1
case2 = [[3,12],[-2,5],[-4,1]]
o2 = 18
assert s.minCostConnectPoints(case2) == o2