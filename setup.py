#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

version = '1.0.0'

setup(
    name='ckanext-extendedactivity',
    version=version,
    description='Adds support for custom activity events.',
    classifiers=[],
    author='Government of Canada',
    author_email='tk@tkte.ch',
    license='MIT',
    packages=find_packages(),
    namespace_packages=['ckanext'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
    ],
    entry_points=(
        '[ckan.plugins]\n'
        'extendedactivity=ckanext.extendedactivity.plugins:ActivityPlugin'
    )
)
