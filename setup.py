"""Install packages as defined in this file into the Python environment."""
import os

from setuptools import setup, find_packages

changelist = os.environ['changelist']

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()
setup(
    name="lfsdata",
    version=fr"0.0.0{changelist}",
    author="Arusha Developers",
    author_email="info@arusha.dev",
    maintainer="Hamed Khademi Khaledi",
    maintainer_email="khaledihkh@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arushadev/lfsdata",
    packages=find_packages(),
    namespace_packages=['el'],
    install_requires=[
        "setuptools>=45.0",
        "coloredlogs",
        "gitlab",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3.0",
        "Topic :: Utilities",
    ],
    python_requires='>=3.11',
)
