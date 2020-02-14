import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pipeline", # Replace with your own username
    version="0.0.1",
    author="Alex Shires",
    author_email="a.shires@gmail.com",
    description="Demo Pipeline",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alexshires/mlops",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)