def extract_title(markdown):
    lines = markdown.split('\n')
    for line in lines:
        if line.startswith('# '):
            return line[2:].strip()
    raise Exception("No H1 header found")

# Unit tests for extract_title
import unittest

class TestExtractTitle(unittest.TestCase):
    def test_extract_title_with_h1(self):
        self.assertEqual(extract_title("# Hello"), "Hello")
        self.assertEqual(extract_title("# Hello World"), "Hello World")
        self.assertEqual(extract_title("#   Hello   "), "Hello")

    def test_extract_title_without_h1(self):
        with self.assertRaises(Exception):
            extract_title("## Hello")
        with self.assertRaises(Exception):
            extract_title("Hello")

if __name__ == "__main__":
    unittest.main()