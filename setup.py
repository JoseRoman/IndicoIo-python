"""
Setup for indicoio apis
"""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="IndicoIo",
    version='0.3.3',
    packages=[
        "IndicoIo",
        "IndicoIo.text",
        "IndicoIo.images",
        "IndicoIo.utils",
        "tests",
    ],
    description="""
        A Python Wrapper for IndicoIo.
        Use pre-built state of the art machine learning algorithms with a single line of code.
    """,
    license="MIT License (See LICENSE)",
    long_description=open("README").read(),
    url="https://github.com/IndicoDataSolutions/IndicoIo-python",
    author="Alec Radford, Slater Victoroff, Aidan McLaughlin",
    author_email="""
        Alec Radford <alec@indicodatasolutions.com>,
        Slater Victoroff <slater@indicodatasolutions.com>,
        Aidan McLaughlin <aidan@indicodatasolutions.com>
    """,
)
