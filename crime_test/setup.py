from setuptools import setup, find_packages

setup(
    name='crime_test',
    version='0.1',
    packages=find_packages(),
    install_requires=['pandas'],
    description='A package for validating and analyzing crime data.',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/crime_test',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
