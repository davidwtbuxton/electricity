from setuptools import setup

import electricity


setup(
    name='electricity',
    version=electricity.__version__,
    description='A static site generator.',
    author='David Buxton',
    author_email='david@gasmark6.com',
    packages=['electricity'],
)
