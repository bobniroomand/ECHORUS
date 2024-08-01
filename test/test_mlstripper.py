import unittest
from io import StringIO
from html.parser import HTMLParser
from mlstriper import strip_tags

class TestMLStriper(unittest.TestCase):

    def test_strip_tags(self):
        html = "<html><head><title></title></head><body><p>Hello, <b>world</b>!</p></body></html>"
        expected_output = "Hello, world!"
        result = strip_tags(html)
        self.assertEqual(result, expected_output)

    def test_strip_tags_with_nested_tags(self):
        html = "<div><p>Hello, <span>world</span>!</p></div>"
        expected_output = "Hello, world!"
        result = strip_tags(html)
        self.assertEqual(result, expected_output)

    def test_strip_tags_with_empty_string(self):
        html = ""
        expected_output = ""
        result = strip_tags(html)
        self.assertEqual(result, expected_output)

    def test_strip_tags_with_non_html_input(self):
        html = "This is not HTML"
        expected_output = "This is not HTML"
        result = strip_tags(html)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()