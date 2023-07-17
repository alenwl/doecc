"""
Setup script for doecc (Data Operations Engineer Code Challenge)

"""
import setuptools
from doecc.__init__ import __version__

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

with open("requirements.txt", "r") as requirements_file:
    requirements = list(requirements_file)

setuptools.setup(
    name="doecc",
    version=__version__,
    author="Ander LC.",
    author_email="andrlc@myserver.com",
    description="Data Operations Engineer Code Challenge",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "doecc = doecc.__main__:main",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Development Status :: 1 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Clarify AI developers",
        "Operating System :: OS Independent",
        "License :: Other/Proprietary License",
        "Typing :: Typed",
    ],
    python_requires=">=3.9",
    include_package_data=True,
    install_requires=requirements,
)
