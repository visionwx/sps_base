# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import os
from setuptools import setup, find_packages

PACKAGE = "sps_base"
NAME = "sps_base" or "sps-base"
DESCRIPTION = "SPS Core Base Library for Python"
AUTHOR = "VisionWX"
AUTHOR_EMAIL = ""
URL = "https://github.com/samdychen/sps_base"
VERSION = __import__(PACKAGE).__version__
REQUIRES = [
    "google-cloud-firestore==1.8.1",
    "google-cloud-pubsub"
]

LONG_DESCRIPTION = ''
if os.path.exists('./README.md'):
    with open("README.md", encoding='utf-8') as fp:
        LONG_DESCRIPTION = fp.read()

setup(
    name=NAME,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    packages=find_packages(exclude=["tests*","build","dist","*egg-info*"]),
    include_package_data=True,
    platforms="any",
    install_requires=REQUIRES,
    python_requires=">=3.7",
    zip_safe=False,
    keywords=["sps","sps base"],
)
