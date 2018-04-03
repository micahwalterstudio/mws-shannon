from setuptools import setup, find_packages

packages = find_packages()
desc = open("README.md").read(),

setup(
    name='shannon',
    version='0.1',
    description='',
    author='Micah Walter Studio',
    url='https://github.com/micahwalterstudio/shannon',
    requires=[],
    install_requires=[
        'Pillow',
    ],
    packages=packages,
    scripts=[],
    download_url='https://github.com/micahwalterstudio/shannon/tarball/master',
    license='MIT')