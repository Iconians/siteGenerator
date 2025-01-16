import unittest
from block_to_block_type import block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        block = "# This is a heading"
        self.assertEqual(block_to_block_type(block), 'heading')
        
        block = "## This is a subheading"
        self.assertEqual(block_to_block_type(block), 'heading')
        
    def test_paragraph(self):
        block = "This is a paragraph of text."
        self.assertEqual(block_to_block_type(block), 'paragraph')
        
    def test_code(self):
        block = "```\nThis is a code block\n```"
        self.assertEqual(block_to_block_type(block), 'code')
        
    def test_quote(self):
        block = "> This is a quote block"
        self.assertEqual(block_to_block_type(block), 'quote')
        
    def test_unordered_list(self):
        block = "* This is an unordered list item"
        self.assertEqual(block_to_block_type(block), 'unordered_list')
        
        block = "- This is another unordered list item"
        self.assertEqual(block_to_block_type(block), 'unordered_list')
        
    def test_ordered_list(self):
        block = "1. This is an ordered list item"
        self.assertEqual(block_to_block_type(block), 'ordered_list')
        
        block = "1. First item\n2. Second item\n3. Third item"
        self.assertEqual(block_to_block_type(block), 'ordered_list')

if __name__ == "__main__":
    unittest.main()