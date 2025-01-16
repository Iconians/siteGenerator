from markdown_to_html_node import markdown_to_html_node
from htmlnode import ParentNode
import unittest

def test_markdown_to_html_node(self):
    markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
    
    html_node = markdown_to_html_node(markdown)
    expected_html = """<div><h1>This is a heading</h1><p>This is a paragraph of text. It has some <b>bold</b> and <i>italic</i> words inside of it.</p><ul><li>This is the first list item in a list block</li><li>This is a list item</li><li>This is another list item</li></ul></div>"""
    
    self.assertEqual(html_node.to_html(), expected_html)

def test_markdown_to_html_node_with_code_block(self):
    markdown = """# This is a heading

This is a paragraph of text.
"""
    html_node = markdown_to_html_node(markdown)
    expected_html = """<div><h1>This is a heading</h1><p>This is a paragraph of text.</p><pre><code>if __name__ == "__main__":\n    unittest.main()\n</code></pre></div>"""
    
    self.assertEqual(html_node.to_html(), expected_html)

if __name__ == "__main__":
    unittest.main()