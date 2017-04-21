from setuptools import setup, find_packages
import sys

CLASSIFIERS = """\
Development Status :: 5 - Production/Stable
Intended Audience :: Developers
License :: OSI Approved :: BSD License
Natural Language :: English
Programming Language :: Python
Programming Language :: Python :: 3.6
""".split("\n")


setup(
    name='wsdl-to-tuple',
    version='0.0.1',
    description='WSDL to Synerty VortexJS/VortexPY Writer',
    install_requires=['lxml>=2.2', 'Jinja2', 'python-dateutil'],
    tests_require=['nose>=1.0', 'Sphinx>=1.0'],
    packages=find_packages(),
    include_package_data=True,
    classifiers=CLASSIFIERS
    )
