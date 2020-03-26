# Time To Planet API

An api for that calculates the time it would take for a message sent from Earth to a planet in our
solar system.

## Tech

time_to_planet is a micro python flask api

Currently the api is basically a wrapper over the http://astronomyapi.org. In the future we may
calculate the distance from earth to planets ourselves.

## Dev

### Links

Helpful links:

- https://flask.palletsprojects.com/en/1.1.x/
- https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates

### ClI Commands

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
