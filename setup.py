# To create my machine learning model as a package
import os
from setuptools import find_packages, setup #type: ignore
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(filepath:str)->List[str]:
    """
    This function will read the requirements.txt file
    and return a list of requirements.
    """
    with open('requirements.txt', 'r') as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Akeem Lagundoye',
    author_email='akeemifedayolag@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)