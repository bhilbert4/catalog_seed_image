#! /usr/bin/env python

from setuptools import setup
from setuptools import find_packages

setup(
    name='catalog_seed_image',
    version = '1.0',
    description='Create a seed image for the NIRCam Data Simulator',
    long_description='A tool to create a noiseless countrate seed image, composed of only simulated sources, to be used as input for the NIRCam data simulator. The seed image is created using source catalogs.',
    url='https://github.com/bhilbert4/catalog_seed_image',
    author='Bryan Hilbert',
    author_email='hilbert@stsci.edu',
    keywords = ['astronomy'],
    classifiers = ['Programming Language :: Python'],
    packages = find_packages(),
    install_requires = [],
    include_package_data = True
    )
