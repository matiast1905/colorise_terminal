from setuptools import setup, find_packages
from pathlib import Path

with open(Path(__file__) / "README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="color_terminal",
    version="0.1.0",
    author="Matias Taron Simoes",
    author_email="matiastaron@gmail.com",
    url="https://github.com/matiast1905/color_terminal",
    license="LICENSE",
    description="Color text and background of terminal output",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(where="."),
    package_dir={"": "."},
    include_package_data=True,
    python_requires=">=3.6",
)