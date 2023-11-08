# pull image dari dockerhub
FROM library/python:latest

# set Buffered python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Membuat Environment
ENV VIRTUAL_ENV=/opt/venv

RUN python3 -m venv $VIRTUAL_ENV

# menjalankan environtment
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# proses update dependency di sistem operasi/image docker
RUN apt update -y

# setup working directory
RUN mkdir /app

RUN ls /app
WORKDIR /app

# install dependency
RUN pip install --upgrade pip

# copy requirements
ADD . /app/

RUN pip install -r requirements.txt --no-cache-dir