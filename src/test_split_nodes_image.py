import unittest
from textnode import TextNode, TextType
from split_nodes_image import split_nodes_image

class TestSplitNodesImage(unittest.TestCase):
    def test_split_nodes_image(self):
        node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and more text", TextType.NORMAL)
        new_nodes = split_nodes_image([node])
        expected_nodes = [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("rick roll", TextType.IMAGES, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and more text", TextType.NORMAL),
        ]
        self.assertEqual(new_nodes, expected_nodes)

if __name__ == "__main__":
    unittest.main()