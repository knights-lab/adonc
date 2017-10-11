from setuptools import setup, find_packages
from glob import glob
import os
import platform
import versioneer

__author__ = "Knights Lab"
__copyright__ = "Copyright (c) 2017 --, %s" % __author__
__credits__ = ["Benjamin Hillmann", "Gabe Al-Ghalith"]
__email__ = "hillmannben@gmail.com"
__license__ = "AGPL"
__maintainer__ = "Benjamin Hillmann"

long_description = 'Make a Python module into an executable - (pronounced eggsecutable)
'

setup(
    name='adonc',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages(),
    package_data={},
    url='',
    license=__license__,
    author=__author__,
    author_email=__email__,
    description='',
    long_description=long_description,
    keywords='',
    install_requires=[],
    entry_points={
        'console_scripts': [
            'adonc = adonc.__main__:main',
        ]
    },
)