import unittest
from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.NORMAL),
            TextNode("obi wan image", TextType.IMAGES, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.NORMAL),
            TextNode("link", TextType.LINKS, "https://boot.dev"),
        ]
        self.assertEqual(nodes, expected_nodes)

if __name__ == "__main__":
    unittest.main()