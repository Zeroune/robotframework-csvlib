import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="robotframework-csvlib",
    version="0.0.2",
    author="Zeroune",
    description="CSV library for robotframework written in Python 3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Zeroune/robotframework-csvlib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
)