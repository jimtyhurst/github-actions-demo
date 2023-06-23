# github-actions-demo

Simple demonstration of GitHub Actions.

The application is a simple "Hello World" web service, implemented in
[FastAPI](https://fastapi.tiangolo.com/).
It returns a greeting as a JSON object.

## Developer instructions
To run it locally in your development environment:

```shell
uvicorn main:app --reload
```

To build a Docker image for this application:

```shell
dkr build --rm -t jimtyhurst/github-actions-demo .
```

To run that image:
```shell
docker run -it --rm --publish 8000:80  jimtyhurst/github-actions-demo:latest
```

To test the app from your browser:

```
# Default greeting
http://localhost:8000/greeting

# Specific greeting
http://localhost:8000/greeting/Chris

# API documentation
http://localhost:8000/docs
```

To test the app from the command line, using `curl`:

```shell
curl http://localhost:8000/greeting
```

To run the [hadolint]() linter on the Dockerfile:

```shell
docker run --rm -i hadolint/hadolint < Dockerfile
```

## License
Copyright (c) 2023 Jim Tyhurst

Licensed under the [MIT License](./LICENSE).

