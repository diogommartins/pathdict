import os
from setuptools import setup, find_packages


VERSION = '0.0.9'


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='pathdict',
    version=VERSION,
    packages=find_packages(exclude=['*test*']),
    url='https://github.com/diogommartins/pathdict',
    author='Diogo Magalhaes Martins',
    author_email='magalhaesmartins@icloud.com',
    keywords='collection dictionary dict path dotted mongodb',
    # Generated with: pandoc --from=markdown --to=rst --output=README.rst README.md
    long_description=read('README.rst')
)
