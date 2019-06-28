FROM centos:7

USER root
COPY goenv.sh /etc/profile.d/

WORKDIR /root

RUN yum -y install sqlite git gcc make wget
RUN wget https://dl.google.com/go/go1.10.1.linux-amd64.tar.gz && tar -C /usr/local -xzf go1.10.1.linux-amd64.tar.gz
RUN mkdir $HOME/go
RUN source /etc/profile.d/goenv.sh

# RUN go