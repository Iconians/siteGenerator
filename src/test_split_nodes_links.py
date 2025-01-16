import unittest
from textnode import TextNode, TextType
from split_nodes_links import split_nodes_link

class TestSplitNodesLink(unittest.TestCase):
    def test_split_nodes_link(self):
        node = TextNode("This is text with a [link to boot dev](https://www.boot.dev) and more text", TextType.NORMAL)
        new_nodes = split_nodes_link([node])
        expected_nodes = [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("link to boot dev", TextType.LINKS, "https://www.boot.dev"),
            TextNode(" and more text", TextType.NORMAL),
        ]
        self.assertEqual(new_nodes, expected_nodes)

if __name__ == "__main__":
    unittest.main()