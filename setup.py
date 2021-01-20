import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mayaparser-kovacevicnikola", # Replace with your own username
    version="0.0.1",
    author="Nikola Kovacevic",
    author_email="nikolakovacevic96@gmail.com",
    description="A small maya parsing package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nikolakovacevic/mayaparser",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: WTFPL License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)