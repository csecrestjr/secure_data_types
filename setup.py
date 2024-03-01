#!/usr/bin/env python

from distutils.core import setup

import securetypes

setup(
	name='secure_types',
	version=securetypes.__version__,
	description="securedict implementation, a dict that uses secure " +
		"hashing to stop algorithmic complexity attacks",
	url="https://github.com/csecrestjr/secure_data_types",
	author="Calvin Secrest",
	author_email="dev@calvinsecrest.com",
	classifiers=[
		'Programming Language :: Python :: 2',
		'Development Status :: 3 - Alpha',
		'Operating System :: OS Independent',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
	],
	py_modules=['securetypes', 'test_securetypes'],
)
