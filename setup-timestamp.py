"""
This is the setup file for the package.
"""

from setuptools import find_packages, setup

setup(
    name='timestamp',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)
