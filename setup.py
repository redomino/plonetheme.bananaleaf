from setuptools import setup, find_packages
import os

version = '1.2'

setup(
        name='plonetheme.bananaleaf',
        description='An installable Diazo theme for Plone 4.1',
        long_description=open('README.rst', 'rb').read()+'\n'+
                         open(os.path.join("docs", "INSTALL.txt")).read()+'\n'+
                         open(os.path.join("docs", "HISTORY.txt")).read(),
        version='1.1',
        author='Giacomo Spettoli',
        author_email='giacomo.spettoli@redomino.com',
        url='https://github.com/redomino/plonetheme.bananaleaf',
        packages=find_packages(),
        include_package_data=True,
        namespace_packages=[
            'plonetheme'
            ],
        install_requires=[
            'setuptools',
            'plone.app.theming',
            ],
        classifiers=[
            "Framework :: Plone",
            "Programming Language :: Python",
            ],
        entry_points={
            'z3c.autoinclude.plugin': 'target = plone',
            }
        )


