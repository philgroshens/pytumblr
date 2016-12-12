#!/usr/bin/env python

from setuptools import setup

setup(

    name="PyTumblr",
    version="0.0.6.py3",
    description="A Python API v2 wrapper for Tumblr (updated for Python3 support)",
    author="John Bunting (Python3 changes by github.com/philgroshens)",
    author_email="johnb@tumblr.com",
    url="https://github.com/tumblr/pytumblr",
    packages = ['pytumblr'],
    license = "LICENSE",

    test_suite='nose.collector',

    install_requires = [
        'oauth2',
        'httpretty',
        'tornado'
    ],

    tests_require=[
        'nose',
        'nose-cov',
        'mock'
    ]

)
