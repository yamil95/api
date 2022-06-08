FROM python:3.8-alpine
MAINTAINER CRISTIAN_CONTRERA <cristiancontrera95@gmail.com>

RUN apk update
RUN apk add make automake cmake gcc g++ python3-dev libffi-dev openssl-dev

WORKDIR /app

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN CRYPTOGRAPHY_DONT_BUILD_RUST=1 pip install -r requirements.txt

COPY src/ .

EXPOSE 5000

CMD ["python" , "run.py"]