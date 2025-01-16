import unittest
from textnode import TextNode, TextType
from textNodeTohtmlNode import text_node_to_html_node
from htmlnode import LeafNode

class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text_node_to_html_node(self):
        text_node = TextNode("This is normal text", TextType.NORMAL)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "This is normal text")

        text_node = TextNode("This is bold text", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<b>This is bold text</b>")

        text_node = TextNode("This is italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<i>This is italic text</i>")

        text_node = TextNode("This is code text", TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<code>This is code text</code>")

        text_node = TextNode("This is a link", TextType.LINKS, "https://www.example.com")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<a href="https://www.example.com">This is a link</a>')

        text_node = TextNode("This is an image", TextType.IMAGES, "https://www.example.com/image.png")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<img src="https://www.example.com/image.png" alt="This is an image"/>')

        with self.assertRaises(ValueError):
            text_node = TextNode("This is an unsupported type", "unsupported")
            text_node_to_html_node(text_node)

if __name__ == "__main__":
    unittest.main()