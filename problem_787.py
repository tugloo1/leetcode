from queue import PriorityQueue
from typing import List, Set, Dict
from unittest import TestCase


class EdgeInfo(object):
    def __init__(self, destination: int, cost: int):
        self.destination = destination
        self.cost = cost

    def __hash__(self):
        return hash(self.destination)

    def __eq__(self, other):
        return self.cost == other.cost and self.destination == other.destination


class FlightTicketFinder(object):
    def __init__(self, edge_info: List[List[int]]):
        self.adj_list = self.create_adjaceny_list(edge_info)  # type: Dict[int, Set[EdgeInfo]]

    @staticmethod
    def create_adjaceny_list(edge_info: List[List[int]]) -> Dict[int, Set[EdgeInfo]]:
        adjaceny_list = {}
        for edge in edge_info:
            src, dest, cost = edge[0], edge[1], edge[2]
            if src not in adjaceny_list:
                adjaceny_list[src] = set()
            if dest not in adjaceny_list:
                adjaceny_list[dest] = set()
            edge_info = EdgeInfo(dest, cost)
            adjaceny_list[src].add(edge_info)
        return adjaceny_list

    def find_cheapest_flight(self, src: int, dest: int, max_stops: int):
        if dest not in self.adj_list:
            return -1
        pq = PriorityQueue()
        # A tuple that will be (cost, src, dest, stop_number)
        starting_node = (0, src, src, 0)
        pq.put(starting_node)

        while not pq.empty():
            starting_cost, edge_src, edge_dest, stop_number = pq.get()
            if edge_dest == dest:
                return starting_cost
            if stop_number > max_stops:
                continue
            connections = self.adj_list[edge_dest]
            print('')
            for connection in connections:
                new_node = (starting_cost + connection.cost, edge_dest, connection.destination, stop_number + 1)
                pq.put(new_node)

        return -1


class FlightTicketFinderTest(TestCase):
    def setUp(self):
        input1 = [
            [0, 1, 100],
            [1, 2, 100],
            [0, 2, 500]
        ]
        self.finder = FlightTicketFinder(input1)

    def test_init(self):
        self.assertEqual(self.finder.adj_list, {0: {EdgeInfo(1, 100), EdgeInfo(2, 500)},
                                                1: {EdgeInfo(2, 100)}, 2: set()})

    def test_find_cheapest_flight1(self):
        self.assertEqual(self.finder.find_cheapest_flight(0, 2, 1), 200)

    def test_find_cheapest_flight2(self):
        edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
        finder = FlightTicketFinder(edges)
        self.assertEqual(finder.find_cheapest_flight(0, 2, 0), 500)

    def test_find_cheapest_flight3(self):
        edges = [[1, 2, 10], [2, 0, 7], [1, 3, 8], [4, 0, 10], [3, 4, 2], [4, 2, 10], [0, 3, 3], [3, 1, 6], [2, 4, 5]]
        finder = FlightTicketFinder(edges)
        self.assertEqual(finder.find_cheapest_flight(0, 4, 1), 5)

    def test_find_cheapest_flight4(self):
        edges = [[0, 1, 100], [0, 2, 500], [1, 2, 100], [2, 3, 100]]
        finder = FlightTicketFinder(edges)
        self.assertEqual(finder.find_cheapest_flight(0, 3, 1), 600)

    def test_find_cheapest_flight5(self):
        edges = [[2, 3, 87], [4, 3, 55], [2, 5, 27], [0, 2, 28], [0, 3, 55], [5, 0, 48], [1, 3, 37],
                 [2, 1, 13], [5, 3, 8], [5, 4, 82]]
        finder = FlightTicketFinder(edges)
        self.assertEqual(finder.find_cheapest_flight(0, 3, 0), 55)

    def test_find_cheapest_flight6(self):
        edges = [[0, 1, 5], [1, 2, 5], [0, 3, 2], [3, 1, 2], [1, 4, 1], [4, 2, 1]]
        finder = FlightTicketFinder(edges)
        self.assertEqual(finder.find_cheapest_flight(0, 2, 2), 7)


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        tracker = FlightTicketFinder(flights)
        return tracker.find_cheapest_flight(src, dst, K)


