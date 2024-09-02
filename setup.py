# To create my machine learning model as a package
from setup import find_packages, setup

setup(
    name='mlproject',
    version='0.0.1',
    author='Akeem Lagundoye',
    author_email='akeemifedayolag@gmail.com',
    packages=find_packages(),
    install_requirements=['pandas', 'numpy', 'seaborn']
)