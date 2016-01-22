import io
import unittest

from electricity import posts


class PostsTestCase(unittest.TestCase):
    def test_parse_empty_file_content(self):
        fh = io.BytesIO(b'')
        frontmatter, text = posts.parse_file_contents(fh)

        self.assertEqual(frontmatter, {})
        self.assertEqual(text, b'')

    def test_parse_no_frontmatter(self):
        fh = io.BytesIO(b'The quick brown fox\n')
        frontmatter, text = posts.parse_file_contents(fh)

        self.assertEqual(frontmatter, {})
        self.assertEqual(text, b'The quick brown fox\n')

    def test_parse_with_frontmatter_and_text(self):
        fh = io.BytesIO(
            b'---\n'
            b'layout: post\n'
            b'title: Blogging Like a Hacker\n'
            b'---\n'
            b'The quick brown fox\n'
            b'jumps over the lazy dog.\n'
        )
        frontmatter, text = posts.parse_file_contents(fh)

        self.assertEqual(frontmatter, {'layout': 'post', 'title': 'Blogging Like a Hacker'})
        self.assertEqual(text, b'The quick brown fox\njumps over the lazy dog.\n')
