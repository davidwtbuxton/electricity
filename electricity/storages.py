import mimetypes
import os

from .posts import Post


extra_content_types = (
    ('text/plain', ['.md', '.markdown']),
)
for type_, ext_list in extra_content_types:
    for ext in ext_list:
        mimetypes.add_type(type_, ext, strict=False)


class Storage(object):
    content_types = ('text/plain',)

    def __init__(self, path=b'.'):
        self.path = path

    def find_posts(self):
        text_exts = mimetypes.guess_all_extensions('text/plain', strict=False)
        all_text_files = []

        for root, dirs, files in os.walk(self.path):
            names = [n for n in files if os.path.splitext(n)[1] in text_exts]
            all_text_files.extend(os.path.join(root, n) for n in names)

        return [Post.from_file(filename) for filename in all_text_files]
