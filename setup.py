try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
	name = "IndicoIo",
	version = '0.1.0dev',
	packages = ["IndicoIo",],
	license = "MIT License (See LICENSE)",
	long_description = open("README").read(),
	url = "http://www.indico.io",
	author = "Alec Radford, Slater Victoroff",
	author_email = "Alec Radford <alec@indicodatasolutions.com>, Slater Victoroff <slater@indicodatasolutions.com>",
)
