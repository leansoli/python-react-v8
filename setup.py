#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages


README = open(
    os.path.join(os.path.dirname(__file__), 'README.md'),
    encoding='utf-8').read()
REQUIREMENTS = open(
    os.path.join(os.path.dirname(__file__), 'requirements.txt'),
    encoding='utf-8').read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='python-react-v8',
    version='0.1.0',
    description='Thin wrapper around v8-cffi to render React views server-side.',
    author='Esteban Castro Borsani',
    author_email='ecastroborsani@gmail.com',
    long_description=README,
    url='https://github.com/nitely/python-react-v8',
    packages=find_packages(exclude=['examples']),
    test_suite="runtests.start",
    zip_safe=False,
    install_requires=REQUIREMENTS,
    setup_requires=REQUIREMENTS,
    license='MIT License',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content'])
