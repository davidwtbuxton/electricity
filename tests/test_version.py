import unittest

import electricity


class VersionTestCas(unittest.TestCase):
    def test_version(self):
        self.assertEqual(electricity.__version__, '0.1')
