FROM ubuntu:latest

RUN apt-get update -y -q && \
    apt-get install --no-install-recommends -y -q \
        python3 python3-dev python3-pip curl build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./exporter ./exporter
COPY ./start_exporter.py ./

EXPOSE 8000

CMD python3 start_exporter.py