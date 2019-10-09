#!/usr/bin/python
# -*- encoding: utf-8 -*-
from setuptools import setup, find_packages

version = '0.6.2'

if __name__ == '__main__':
    setup(
        name='carddav',
        version=version,
        description="carddav package from carddav-utils",
        long_description=open("README.md").read(),
        keywords='',
        packages=find_packages(exclude=['tests']),
        include_package_data=True,
        install_require=['lxml', 'vobject', 'requests'],
        zip_safe=False,
    )
