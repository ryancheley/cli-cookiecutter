import io
import os

from setuptools import find_packages, setup

VERSION = "0.0.0"


def get_long_description():
    with io.open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="{{cookiecutter.library_name}}",
    description="{{cookiecutter.library_description}}",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="{{cookiecutter.author_name}}",
    version=VERSION,
    license="Apache License, Version 2.0",
    packages=find_packages(),
    install_requires=[],
    extras_require={"test": ["pytest"]},
    tests_require=["{{cookiecutter.library_name}}[test]"],
    setup_requires=["pytest-runner"],
    entry_points="""
        [console_scripts]
        {{cookiecutter.library_name}}={{cookiecutter.library_folder}}.cli:cli
    """,
    url="https://github.com/ryancheley/{{cookiecutter.library_name}}",
    project_urls={
        "Issues": "https://github.com/ryancheley/{{cookiecutter.library_name}}/issues",
        "CI": "https://github.com/ryancheley/{{cookiecutter.library_name}}/actions",
        "Changelog": "https://github.com/ryancheley/{{cookiecutter.library_name}}/releases",
    },
    python_requires=">=3.7",
)