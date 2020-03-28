# Time To Planet API

An api for that calculates the time it would take for a message sent from Earth to a planet in our
solar system.

> you can check the [CHANGELOG](CHANGELOG.md) to see all the releases

## Tech

time_to_planet is a micro python flask api

Currently the api is basically a wrapper over the http://astronomyapi.org. In the future we may
calculate the distance from earth to planets ourselves.

## Dev

### Links

Helpful links:

- https://flask.palletsprojects.com/en/1.1.x/
- https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates
- https://learnxinyminutes.com/docs/python

### Versioning

This api is visioned with following the [Semantic Versioning](https://semver.org) convention.
Versions can be seen in the [CHANGELOG](CHANGELOG.md) or under [tags](/tags). In order to make this
possible we ask our developers to:

- Follow [conventionalcommits](https://www.conventionalcommits.org/) convention when committing
    - ex. feat(caching): add second cache key
    - ex. fix(time_calc): multiple to get seconds
    - ex. docs: init README.md
    - ex. refactor: init pprint module for printing json
    - ex. test(remote_api): test valid cache flow
    - ex. deploy(0.0.1): ship mvp
- If PR makes significant changes bump version
- When bumping version make sure to update [CHANGELOG](CHANGELOG.md) and apply tag to deploy commit that updates [deployment.yml](deploy/deployment.yml)
    - ex. deploy(0.0.1): ship mvp

### CLI Commands

**Run app:**

```shell
$ FLASK_APP=time_to_planet.py flask run
```

**Virtual Env:**

Init virtual env with:

```shell
$ python3 -m venv venv
```

Then to activate it

```shell
$ source ./venv/bin/activate
```

**Unit Testing:**

Run Unit tests with:

```shell
$ python -m unittest
```

**Installing new packages:**

```shell
$ pipenv install requests
```

**Running mock astronomyapi server:**

Currently we get out distance numbers to calculate time from an external api. To mock this on local
we use a node module, json-server.

```shell
$ npx json-server --watch astronomy_api_mock.json
```

**Install existing packages:**

```shell
$ pipenv sync
```

**Format Code:**

```shell
$ autopep8 --in-place --aggressive --aggressive ./app/**/*.py
```
