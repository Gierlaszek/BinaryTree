from unittest import TestCase
from BT import BinaryTree




class TestBinaryTree(TestCase):
    def setUp(self):
        self.tree = BinaryTree(5)

    def test_print_tree(self):
        value = self.tree.print_tree()
        self.assertEqual(type(value), list, "Wrong type, expected List")
        self.assertTrue(value)

    def test_pre_order(self):
        value = self.tree.pre_order(self.tree.root, [])
        self.assertEqual(value, [5], "Incorrect value")

    def test_searchNode(self):
        value = self.tree.pre_order(self.tree.root, 5)
        self.assertEqual(type(value), dict, "Wrong type, expected dict")

    def test_calculations(self):
        value = self.tree.calculations(self.tree.root)
        self.assertEqual(type(value), dict , "Incorrect value")


