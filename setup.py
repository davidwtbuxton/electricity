from setuptools import setup
import sys

import electricity


# Tell Python27 we need mock to run tests with `python setup.py test`
tests_require = ['mock'] if sys.version_info.major < 3 else []


setup(
    name='electricity',
    version=electricity.__version__,
    description='A static site generator.',
    author='David Buxton',
    author_email='david@gasmark6.com',
    packages=[
        'electricity',
        'electricity.tests',
    ],
    install_requires=[
        'PyYAML>=3.08',
        'six',
    ],
    test_suite='electricity.tests',
    tests_require=tests_require,
)
