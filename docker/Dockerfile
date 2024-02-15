FROM ubuntu:latest

RUN apt-get update -y -q && \
    apt-get install --no-install-recommends -y -q \
        python3 python3-pip curl build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -LO https://github.com/prometheus/node_exporter/releases/download/v1.7.0/node_exporter-1.7.0.linux-amd64.tar.gz && \
    tar xvf node_exporter-1.7.0.linux-amd64.tar.gz && \
    cp node_exporter-1.7.0.linux-amd64/node_exporter /usr/local/bin

RUN apt-get install -y nginx

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./exporter ./exporter
COPY ./start_exporter.py ./

EXPOSE 8000

EXPOSE 80

EXPOSE 9100

CMD python3 start_exporter.py && node_exporter && service nginx start 
