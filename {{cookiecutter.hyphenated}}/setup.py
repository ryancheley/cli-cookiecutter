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
    name="{{cookiecutter.hyphenated}}",
    description="{{cookiecutter.library_description}}",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="{{cookiecutter.author_name}}",
    version=VERSION,
    license="Apache License, Version 2.0",
    packages=find_packages(),
    install_requires=["click", "rich"],
    extras_require={"test": ["pytest", "black", "isort", "coverage", "mypy", "cogapp"]},
    tests_require=["{{cookiecutter.hyphenated}}[test]"],
    setup_requires=["pytest-runner"],
    entry_points="""
        [console_scripts]
        {{cookiecutter.hyphenated}}={{cookiecutter.underscored}}.cli:cli
    """,
    url="https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.hyphenated}}",
    project_urls={
        "Issues": "https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.hyphenated}}/issues",
        "CI": "https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.hyphenated}}/actions",
        "Changelog": "https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.hyphenated}}/releases",
    },
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)