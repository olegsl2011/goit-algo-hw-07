import random
import unittest

from avl_tree import AVLTree


def random_int_list(min_len, max_len, min_val, max_val):
    
    if min_len < 0 or max_len < min_len or min_val > max_val:
        raise ValueError("Invalid input parameters")

    length = random.randint(min_len, max_len)
    return [random.randint(min_val, max_val) for _ in range(length)]


class AVLTreeTest(unittest.TestCase):

    def test_get_max_value_node(self):
        for i in range(1, 1000):
            tree = AVLTree()
            root = None
            nums = random_int_list(1, 100, 1, 100)
            max_num = max(nums)

            for num in nums:
                root = tree.insert_node(root, num)

            self.assertEqual(max_num, tree.get_max_value_node(root).key,
                             f"Error on iteration {i}:\nmax_value: {max_num}\nnums: {nums}\n")

    def test_get_min_value_node(self):
        for i in range(1, 1000):
            tree = AVLTree()
            root = None
            nums = random_int_list(1, 100, 1, 100)
            min_num = min(nums)

            for num in nums:
                root = tree.insert_node(root, num)

            self.assertEqual(min_num, tree.get_min_value_node(root).key,
                             f"Error on iteration {i}:\nmin_value: {min_num}\nnums: {nums}\n")

    def test_get_nodes_values_sum(self):
        for i in range(1, 1000):
            tree = AVLTree()
            root = None
            nums = random_int_list(1, 100, 1, 100)
            nums_sum = sum(nums)

            for num in nums:
                root = tree.insert_node(root, num)

            self.assertEqual(nums_sum, tree.get_nodes_values_sum(root),
                             f"Error on iteration {i}:\nsum: {nums_sum}\nnums: {nums}\n")

    def test_insertion_and_deletion(self):
        tree = AVLTree()
        root = None

        nums = []

        for i in range(1, 1000):
            num = random.randint(1, 100)

            root = tree.insert_node(root, num)
            nums.append(num)

            should_be_deletion = random.choice([True, False])

            if should_be_deletion:
                num = random.choice(nums)
                root = tree.delete_node(root, num)
                nums.remove(num)

            nums_sum = sum(nums)

            self.assertEqual(nums_sum, tree.get_nodes_values_sum(root),
                             f"Inconsistency found on iteration {i}:\nsum: {nums_sum}\nnums: {nums}\n")


if __name__ == '__main__':
    unittest.main()
