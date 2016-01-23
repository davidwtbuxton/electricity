import itertools

import yaml

from . import utils


class Post(object):
    def __init__(self, text=b'', frontmatter=None):
        self.text = text
        self.frontmatter = frontmatter or {}

    @classmethod
    def from_file(cls, filename):
        with utils.open_filename(filename, 'rU') as fh:
            frontmatter, text = parse_file_contents(fh)

        return cls(text=text, frontmatter=frontmatter)


def parse_file_contents(lines):
    """Parses a string, looking for YAML frontmatter. Returns a pair of
    (dict, text).
    """
    # http://jekyllrb.com/docs/frontmatter/
    frontmatter = {}

    try:
        first_line = next(lines)
    except StopIteration:
        return frontmatter, b''

    if first_line.strip() == b'---':
        yaml_lines = itertools.takewhile(lambda x: x.strip() != b'---', lines)
        yaml_lines = b''.join(yaml_lines)
        frontmatter = yaml.safe_load(yaml_lines)
        content_lines = b''.join(lines)
    else:
        content_lines = first_line + b''.join(lines)

    return frontmatter, content_lines
