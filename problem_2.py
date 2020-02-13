from unittest import TestCase


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node_a, node_b = l1, l2
        starting_node = None
        carry_over = 0
        last_node = None
        while node_a is not None or node_b is not None:
            place_sum = carry_over
            if node_a:
                place_sum += node_a.val
                node_a = node_a.next
            if node_b:
                place_sum += node_b.val
                node_b = node_b.next
            if place_sum > 9:
                place_sum = place_sum - 10
                carry_over = 1
            else:
                carry_over = 0
            new_node = ListNode(place_sum)
            if starting_node is None:
                starting_node = ListNode(place_sum)
                last_node = starting_node
            else:
                last_node.next = new_node
                last_node = new_node
            if carry_over:
                new_node = ListNode(carry_over)
                last_node.next = new_node
        return starting_node

    @staticmethod
    def convert_seq_to_linked_list(seq):
        starting_node = ListNode(seq[0])
        last_node = starting_node
        for i in range(1, len(seq)):
            node = ListNode(seq[i])
            last_node.next = node
            last_node = node
        return starting_node


class SolutionTest(TestCase):
    def test1(self):
        one = Solution.convert_seq_to_linked_list([2, 4, 3])
        two = Solution.convert_seq_to_linked_list([5, 6, 4])
        output = Solution().addTwoNumbers(one, two)
        return

