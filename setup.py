"""Python setup.py for template_gen_1 package"""
import io
import os
from setuptools import find_packages, setup


def read(*names, **kwargs):
    """Read a file."""
    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


setup(
    name="template_gen_1",
    version="0.1.0",
    description="Awesome template_gen_1 created by jefmud",
    url="https://github.com/jefmud/template_gen_1/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="jefmud",
    packages=find_packages(exclude=["tests"]),
    install_requires=[],
    entry_points={
        "console_scripts": ["template_gen_1 = template_gen_1.__main__:main"]
    },
    extras_require={
        "test": [
            "pytest",
            "coverage",
            "flake8",
            "black",
            "isort",
            "pytest-cov",
            "codecov",
            "mypy",
            "gitchangelog",
            "mkdocs",
        ],
    },
)
