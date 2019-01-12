#!/usr/bin/env python
from setuptools import setup
from setuptools.command import easy_install
from setuptools.command.install import install

VERSION = '2.1.0-rc3'


class InstallDefaultDecoder(install):

    def run(self):
        try:
            try:
                import text_unidecode
            except ImportError:
                import unidecode
        except ImportError:
            # TODO: Find a way to log output to console
            easy_install.main(self.distribution.extras_require['unidecode'])
        install.run(self)


setup(
    name='python-slugify2',
    version=VERSION,
    packages=['slugify'],
    url='https://github.com/roniemartinez/python-slugify2',
    download_url='https://github.com/roniemartinez/python-slugify2/tarball/{}'.format(VERSION),
    license='MIT',
    author='Ronie Martinez',
    author_email='ronmarti18@gmail.com',
    description='Fork of un33k/python-slugify to fix issue #68',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords=[],
    cmdclass={
        'install': InstallDefaultDecoder
    },
    extras_require={
        'unidecode': 'Unidecode>=0.04.16',
        'text-unidecode': 'text-unidecode==1.2'
    },
    entry_points={'console_scripts': ['slugify=slugify.slugify:main']},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython'
    ]
)
