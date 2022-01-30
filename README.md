# CLI Cookiecutter

This is the Cookiecutter template that **I** use when creating a CLI apps. It's set up for my tastes. PRs will be considered, but if you like the base and want to make it your own, I encourage you to fork it! That way, you get what you want, and I get what I want. Everybody wins 😊

This CLI will include the following packages:

- [click](https://pypi.org/project/click/)
- [rich](https://pypi.org/project/rich/)

The CLI will include the following packages for testing:

- [pytest](https://pypi.org/project/pytest/)
- [black](https://pypi.org/project/black/)
- [isort](https://pypi.org/project/isort/)
- [coverage](https://pypi.org/project/coverage/)
- [mypy](https://pypi.org/project/mypy/)
- [cogapp](https://pypi.org/project/cogapp/)

In order for this to be able to deploy to [PyPi](https://pypi.org) you'll need to add an Actions Secret called `PYPI_TOKEN`. If that isn't done, the publishing workflow will fail. 

