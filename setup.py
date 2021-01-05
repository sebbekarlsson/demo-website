from setuptools import setup, find_packages


setup(
    name="demowebsite",
    version='1.0.0',
    install_requires=['flask', 'pytest'],
    packages=find_packages(),
)