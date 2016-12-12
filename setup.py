#!/usr/bin/env python

from setuptools import setup

setup(

    name="PyTumblr",
    version="0.0.7",
    description="A Python API v2 wrapper for Tumblr (updated for Python3 support)",
    author="Phil Groshens (Original wrapper by John Bunting (johnb@tumblr.com))",
    author_email="offerhero@gmail.com",
    url="https://github.com/philgroshens/pytumblr",
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
