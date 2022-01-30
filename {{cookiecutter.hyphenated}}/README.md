# {{cookiecutter.hyphenated}}

[![PyPI](https://img.shields.io/pypi/v/# {{cookiecutter.hyphenated}}.svg)](https://pypi.org/project/# {{cookiecutter.hyphenated}}/)
[![GitHub changelog](https://img.shields.io/github/v/release/{{cookiecutter.github_username}}/# {{cookiecutter.hyphenated}}?include_prereleases&label=changelog)](https://github.com/{{cookiecutter.github_username}}/# {{cookiecutter.hyphenated}}/releases)
[![Tests](https://github.com/{{cookiecutter.github_username}}/# {{cookiecutter.hyphenated}}/workflows/Test/badge.svg)](https://github.com/{{cookiecutter.github_username}}/# {{cookiecutter.hyphenated}}/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/{{cookiecutter.github_username}}/# {{cookiecutter.hyphenated}}/blob/main/LICENSE)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/{{cookiecutter.github_username}}/# {{cookiecutter.hyphenated}}/main.svg)](https://results.pre-commit.ci/latest/github/{{cookiecutter.github_username}}/# {{cookiecutter.hyphenated}}/main)


{{cookiecutter.description}}

## How to install

    $ pip install {{cookiecutter.hyphenated}}

## Usage


## # {{cookiecutter.hyphenated}} --help

<!-- [[[cog
import cog
from # {{cookiecutter.underscored}} import cli
from click.testing import CliRunner
runner = CliRunner()
result = runner.invoke(cli.cli, ["--help"])
help = result.output.replace("Usage: cli", "Usage: # {{cookiecutter.hyphenated}}")
cog.out(
    "```\n{}\n```".format(help)
)
]]] -->
```


```
<!-- [[[end]]] -->
