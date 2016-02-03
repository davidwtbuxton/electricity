import io
import os
import tempfile
import unittest

from electricity import utils


class OpenFilenameTestCase(unittest.TestCase):
    def setUp(self):
        super(OpenFilenameTestCase, self).setUp()
        _, self.test_tempfile_name = tempfile.mkstemp()

    def tearDown(self):
        super(OpenFilenameTestCase, self).tearDown()
        os.unlink(self.test_tempfile_name)

    def test_opens_filename_by_string(self):
        # If the argument is a string, then open the named file, close it on exit.

        # N.B. Opening as binary so Py3 doesn't decode it automatically.
        with utils.open_filename(self.test_tempfile_name, 'rb') as fh:
            text = fh.read()

            self.assertEqual(text, b'')

    def test_opens_file_like_object(self):
        fileobj = io.BytesIO(b'')

        with utils.open_filename(fileobj) as fh:
            text = fh.read()

            self.assertEqual(text, b'')

        self.assertFalse(fileobj.closed)

    def test_opens_and_closes_file_like_object(self):
        fileobj = io.BytesIO(b'')

        with utils.open_filename(fileobj, closing=True) as fh:
            text = fh.read()

            self.assertEqual(text, b'')

        self.assertTrue(fileobj.closed)
