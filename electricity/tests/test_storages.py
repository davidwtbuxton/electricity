import unittest

try:
    import unittest.mock as mock
except ImportError:
    import mock

from electricity import storages


class StorageTestCase(unittest.TestCase):
    def test_find_posts(self):
        mock_walk = (
            ('/home', ['one'], ['foo.txt']),
            ('/home/one', [], ['bar.html', 'baz.md']),
        )
        with mock.patch('os.walk') as w, mock.patch('electricity.posts.Post.from_file') as p:
            w.return_value = mock_walk

            obj = storages.Storage(path='/home')
            posts = obj.find_posts()

        self.assertEqual(
            p.call_args_list,
            [mock.call('/home/foo.txt'), mock.call('/home/one/baz.md')],
        )
