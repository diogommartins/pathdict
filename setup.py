from setuptools import setup, find_packages


VERSION = '0.0.1'


setup(name='pathdict',
      version=VERSION,
      packages=find_packages(exclude=['*test*']),
      url='https://github.com/diogommartins/pathdict',
      author='Diogo Magalhães Martins',
      author_email='magalhaesmartins@icloud.com',
      keywords='collection dictionary dict path dotted')