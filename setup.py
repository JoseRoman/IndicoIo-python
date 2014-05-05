try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
	name = "IndicoIo",
	version = '0.2.2',
	packages = ["IndicoIo",],
	license = "MIT License (See LICENSE)",
	long_description = open("README.md").read(),
	url = "https://github.com/IndicoDataSolutions/IndicoIo-python",
	author = "Alec Radford, Slater Victoroff",
	author_email = "Alec Radford <alec@indicodatasolutions.com>, Slater Victoroff <slater@indicodatasolutions.com>",
)
