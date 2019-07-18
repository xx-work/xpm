FROM alpine:3.10
MAINTAINER actanble <actanble@gmail.com>

USER root

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories
RUN apk add --no-cache -U gcc make wget perl file autoconf linux-headers
#RUN apk add --no-cache -U libc-dev ncurses-dev

ARG SNMP_VERSION=5.8
RUN mkdir -p /snmpd
WORKDIR /snmpd

RUN wget https://nchc.dl.sourceforge.net/project/net-snmp/net-snmp/${SNMP_VERSION}/net-snmp-${SNMP_VERSION}.tar.gz && \
tar zxvf net-snmp-${SNMP_VERSION}.tar.gz && \
cd net-snmp-${SNMP_VERSION} && \
./configure --prefix=/snmpd \
--enable-mfd-rewrites \
--with-default-snmp-version=2 \
--with-sys-contact=actanble@gmail.com \
--with-sys-location=China \
--with-logfile=/snmpd/var/snmpd.log \
--with-persistent-directory=/snmpd/var/net-snmp && make && make install

#RUN ln -sn /snmpd/sbin/snmpd /usr/bin/snmpd && ln -sn /snmpd/sbin/snmptrapd /usr/bin/snmptrapd

RUN apk add --no-cache tini
ENTRYPOINT ["/sbin/tini", "-vvv", "-g", "-w", "--"]
RUN groupadd -r snmp && useradd -r -g snmp snmp \
    && chown -R snmp /snmpd /tini && chgrp -R snmp /snmpd /tini
USER snmp
WORKDIR /snmpd
EXPOSE 161 162
CMD ['/snmpd/sbin/snmpd', '-C', '-c', '-f', '/snmpd/snmpd.conf']


# NOTE: docker run -it --rm registry.cn-beijing.aliyuncs.com/xx-z/net-snmp:v1 /snmpd/snmpd -h
# docker ps -a | grep snmp | awk '{print $1}' | xargs docker stop | xargs docker rm