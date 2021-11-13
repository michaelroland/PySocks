#!/usr/bin/env python
import os
import re
from setuptools import setup

base_path = os.path.dirname(__file__)

with open("README.md") as f:
    long_description = f.read()


with open(os.path.join(base_path, "socks.py")) as f:
    VERSION = re.compile(r'.*__version__ = "(.*?)"', re.S).match(f.read()).group(1)

setup(
    name="PySocks",
    version=VERSION,
    description="A Python SOCKS client module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/urllib3/PySocks",
    license="BSD-3",
    author="Anorov",
    author_email="anorov.vorona@gmail.com",
    maintainer="urllib3 team",
    maintainer_email="sethmichaellarson@gmail.com",
    keywords=["socks", "proxy"],
    py_modules=["socks", "sockshandler"],
    install_requires=["win-inet-pton; python_version<'3' and os_name=='nt'"],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    classifiers=(
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Internet :: Proxy Servers",
        "Topic :: Internet :: WWW/HTTP",
    ),
)
