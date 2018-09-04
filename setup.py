import os

from setuptools import find_packages, setup

DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(DIR, 'test_requirements.txt')) as req_file:
    tests_require = req_file.readlines()

with open(os.path.join(DIR, 'requirements.txt')) as req_file:
    install_requires = req_file.readlines()

setup(
    name='jsonlogic-transpiler',
    version='1.0.0',
    description='JsonLogic Transpiler',
    url='https://github.com/mmniazi/jsonlogic-transpiler',
    author='Mohsin Niazi',
    author_email='muhammad.mohsin1994@gmail.com',
    license='MIT',
    packages=find_packages(exclude=['tests', 'tests.*']),
    install_requires=install_requires,
    tests_require=tests_require
)
