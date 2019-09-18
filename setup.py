#!/usr/bin/env python

from setuptools import setup, find_packages

PROJECT = 'myapp'
VERSION = '0.1'

try:
    long_description = open('README.md', 'rt').read()
except IOError:
    long_description = ''

setup(
    name=PROJECT,
    version=VERSION,

    description='This is my awesome cli app',
    long_description=long_description,

    author='...',
    author_email='...',

    url='...',

    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Environment :: Console',
    ],

    install_requires=[
        'cliff'
    ],

    tests_require=[
        'setuptools-lint',
        'nose'
    ],

    test_suite='nose.collector',

    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'myapp = myapp.app:run'
        ],
        'myapp': [
            'somecommand = myapp.dummy:NoImplemented',
            'debug = dbtool.dummy:Debug',
        ],
    },

    zip_safe=False,
)
