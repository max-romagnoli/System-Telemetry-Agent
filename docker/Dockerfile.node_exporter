FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y nginx

RUN apt-get install -y curl && \
    curl -LO https://github.com/prometheus/node_exporter/releases/download/v1.7.0/node_exporter-1.7.0.linux-amd64.tar.gz && \
    tar xvf node_exporter-1.7.0.linux-amd64.tar.gz && \
    cp node_exporter-1.7.0.linux-amd64/node_exporter /usr/local/bin

EXPOSE 80

EXPOSE 9100

CMD service nginx start && node_exporter