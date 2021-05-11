from setuptools import setup, find_packages

with open('README_pkg.md') as readme_file:
    readme = readme_file.read()

setup(
    version='0.1.2',
    name='line-segment-intersections',
    author="Liah Carpenter and Aaron Ott",
    url='https://github.com/LiahNikol/line-segment-intersections',
    description="Implementation of Bentley-Ottman algorithm for finding line segment intersections.",
    install_requires=['numpy >= 1.19.0'],
    license="MIT license",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    
)