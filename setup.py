# -*- coding: utf-8 -*-
"""\
=====================
london-fun
=====================

London Fun
"""

import os
from setuptools import setup, find_packages

version = '1.0.0'

this_directory = os.path.abspath(os.path.dirname(__file__))


def read(*names):
    return open(os.path.join(this_directory, *names), 'r').read().strip()


dev_require = [
    'django',
    'flask',
    'flask-sqlalchemy',
    'psycopg2',
]
long_description = '\n\n'.join(
    [read(*paths) for paths in (('README.md',),
                                ('doc', 'contributors.rst'),
                                ('doc', 'changes.rst'))]
    )

setup(
    name='london-fun',
    version=version,
    description='A map of fun things to do in London',
    long_description=long_description,
    author='Georgina Steele',
    author_email='georginamsteele@gmail.com',
    classifiers=[
            "Programming Language :: Python",
        ],
    keywords='london fun web app',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=dev_require,
    tests_require=dev_require,
)
