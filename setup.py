#!/usr/bin/env python
# -*- coding: utf-8 -*-

import carbon_client

from codecs import open

try:
    from setuptools import setup
except ImportError:
    from distutils import setup

packages = [
    'carbon_client'
    ]

requires = []

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name='carbon_client',
    version=carbon_client.__version__,
    description='Send metrics to graphite-carbon.',
    long_description=readme,
    author=carbon_client.__author__,
    author_email='andreas@smaato.com',
    url='https://github.com/smaato/carbon-client',
    packages=packages,
    package_data={'':['LICENSE']},
    package_dir={'carbon_client': 'carbon_client'},
    include_package_data=True,
    install_requires=requires,
    license='MIT',
    zip_safe=False,
    classifiers=(
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7'
    )
)
