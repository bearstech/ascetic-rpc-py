# -*- coding: utf-8 -*-
import os
from setuptools import setup
from setuptools import find_packages

version = '0.2.dev0'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


setup(
    name='ascetic_rpc',
    version=version,
    description="Ascetic RPC",
    #long_description=read('README.rst'),
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='',
    author='Mathieu Lecarme',
    author_email='mlecarme@bearstech.com',
    #packages=find_packages(exclude=['docs', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'protobuf',
    ],
    extras_require={
    },
)
