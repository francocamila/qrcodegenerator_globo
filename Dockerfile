FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /qrcode
WORKDIR /qrcode
COPY requirements.txt /qrcode/
RUN pip install -r requirements.txt
COPY . /qrcode/