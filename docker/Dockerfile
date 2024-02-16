FROM python:3.11-slim-bullseye

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

# RUN echo $PWD

COPY requirements.txt /tmp/pip/requirements.txt

# update system and certificates
RUN apt-get update \
    && apt-get install --no-install-recommends -y\
       ca-certificates  \
       p7zip-full \
       zip \
    && update-ca-certificates \
    && python -m pip install -r /tmp/pip/requirements.txt \
    && rm -rf /var/lib/apt/lists/*
