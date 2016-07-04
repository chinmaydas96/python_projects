#!/usr/bin/env python

from setuptools import setup, find_packages


version = '0.1.0'

setup(
    name='shape_class',
    version=version,
    description='hello world',
    long_description='',
    author='Chinmay Das',
    author_email='chinmaydasbat@gmail.com',
    license='MIT',
    keywords=['command line', 'cli'],
    url='https://github.com/chinmaydas96',
    packages=find_packages(),
    install_requires=[],
)

print find_packages()