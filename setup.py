#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup


description = "Bottle plugin beaker, WSGI middleware for sessions and caching"

setup(
    name='bottle-beaker',
    version="0.1.0",
    description=description,
    author="Thiago Avelino",
    author_email="thiago@avelino.xxx",
    license='MIT',
    platforms='any',
    zip_safe=False,
    url='https://github.com/avelino/bottle-beaker',
    py_modules=['bottle_beaker'],

    classifiers=[
        'Environment :: Web Environment',
        'Environment :: Plugins',
        'Framework :: Bottle',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)