FROM python:3.6-slim-jessie

RUN rm /etc/apt/sources.list
RUN echo "deb http://deb.debian.org/debian/ jessie main contrib non-free" >> /etc/apt/sources.list
RUN echo "deb-src http://deb.debian.org/debian/ jessie main contrib non-free" >> /etc/apt/sources.list
RUN echo "deb http://security.debian.org/ jessie/updates main contrib non-free" >> /etc/apt/sources.list
RUN echo "deb-src http://security.debian.org/ jessie/updates main contrib non-free" >> /etc/apt/sources.list


RUN apt-get update -yqq \
    && apt-get install -yqq --no-install-recommends \
        build-essential \
        git \
        htop \
        libmysqlclient-dev \
        libsnappy-dev \
        libsasl2-modules \
        libsasl2-dev \
        libsasl2-modules-gssapi-mit \
        nano \
        python3-dev \
    && pip install \
        ansible \
        Cython \
    && apt-get clean \
    && rm -rf \
        /tmp/* \
        /usr/share/doc \
        /usr/share/doc-base \
        /usr/share/man \
        /var/lib/apt/lists/* \
        /var/tmp/*

ENV DEBIAN_FRONTEND noninteractive
ENV PATH="/opt/program:${PATH}"
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PYTHONUNBUFFERED=TRUE
ENV TERM linux

# requirements
COPY requirements.txt .
RUN pip install -U pip \
    && pip install -r requirements.txt

RUN mkdir /topics

COPY . ./topics
