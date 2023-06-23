# To build:
# docker build --rm -t jimtyhurst/github-actions-demo .
#
# To run:
# docker run -it --rm --publish 8000:80  jimtyhurst/github-actions-demo:latest
#
# Notes:
#   --it  interactive with tty access.
#   --rm  removes/deletes the container when it is finished running.
#   --publish 8000:80  exposing container's port 80 as port 8000 on the machine that is running the container.

FROM python:3.10.12-bookworm

WORKDIR /web-service

COPY ./requirements.txt /web-service/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /web-service/requirements.txt

COPY ./app /web-service/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
