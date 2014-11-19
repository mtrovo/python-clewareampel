#!/usr/bin/env python

from setuptools import setup

import clewareampel


setup(
    name='clewareampel',
    version=clewareampel.__version__,
    description='Control the Cleware USB Ampel (traffic lights) with Python.',
    long_description='Control the Cleware USB Ampel (traffic lights) with '
                     'Python.',
    author='Roderick Baier',
    author_email='roderick.baier@gmail.com',
    license='MIT',
    url='https://github.com/rbaier/python-clewareampel',
    py_modules=['clewareampel'],
    install_requires=[
        'pyusb'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: System :: Hardware :: Hardware Drivers',
        'Topic :: Utilities'
    ],
    entry_points={
        'console_scripts': [
            'clewareampel=clewareampel:main',
        ]
    }
)
