
import unittest
from unittest.mock import patch
from io import StringIO
import sys

# Assuming the code above is in a file named phonelist.py
from phonelist import SuffixTreeNode, SuffixTree, main

class TestPhoneList(unittest.TestCase):

    def test_SuffixTreeNode(self):
        node = SuffixTreeNode()
        self.assertEqual(node.children, {})
        self.assertEqual(node.is_end, False)

    def test_SuffixTree(self):
        tree = SuffixTree()
        self.assertIsInstance(tree.root, SuffixTreeNode)

        self.assertEqual(tree.insert('123'), False)
        self.assertEqual(tree.insert('1234'), True)

    @patch('builtins.input', side_effect=['2', '3', '911', '97625999', '91125426', '5', '113', '12340', '1234', '12345', '98346', '123'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main(self, mock_stdout, mock_input):
        main()
        self.assertEqual(mock_stdout.getvalue(), 'YES\nNO\n')

if __name__ == '__main__':
    unittest.main()