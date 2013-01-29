from distutils.core import setup

setup(
    name='quicksync',
    version='0.1.0',
    author='Spencer Herzberg',
    author_email='spencer.herzberg@gmail.com',
    packages=['quicksync',],
    scripts=['bin/quicksync',],
    license='LICENSE.txt',
    description='Folder syncing tool',
    long_description=open('README.rst').read(),
)
