import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node1 = HTMLNode(tag="a", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node1.props_to_html(), ' href="https://www.google.com" target="_blank"')

        node2 = HTMLNode(tag="img", props={"src": "image.png", "alt": "An image"})
        self.assertEqual(node2.props_to_html(), ' src="image.png" alt="An image"')

        node3 = HTMLNode(tag="div", props={})
        self.assertEqual(node3.props_to_html(), '')

        node4 = HTMLNode(tag="p")
        self.assertEqual(node4.props_to_html(), '')

    def test_leafnode_to_html(self):
        node1 = LeafNode(tag="span", value="Hello, world!", props={"class": "highlight"})
        self.assertEqual(node1.to_html(), '<span class="highlight">Hello, world!</span>')

        node2 = LeafNode(tag=None, value="Just text")
        self.assertEqual(node2.to_html(), 'Just text')

        with self.assertRaises(ValueError):
            LeafNode(tag="p", value=None)
    
    def test_parentnode_to_html(self):
        child1 = LeafNode(tag="span", value="Child 1")
        child2 = LeafNode(tag="span", value="Child 2")
        parent = ParentNode(tag="div", children=[child1, child2], props={"class": "parent"})
        self.assertEqual(parent.to_html(), '<div class="parent"><span>Child 1</span><span>Child 2</span></div>')

        with self.assertRaises(ValueError):
            ParentNode(tag=None, children=[child1, child2])

        with self.assertRaises(ValueError):
            ParentNode(tag="div", children=None)

if __name__ == "__main__":
    unittest.main()