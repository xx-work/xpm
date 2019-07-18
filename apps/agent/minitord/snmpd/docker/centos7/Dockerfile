FROM centos:7
MAINTAINER actanble <actanble@gmail.com>

USER root

RUN yum install yum-fastestmirror -y
RUN yum -y install locales gcc make wget perl perl-devel file
RUN localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8

## Linux Common
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

RUN cp /snmpd/net-snmp-${SNMP_VERSION}/EXAMPLE.conf /snmpd/snmpd.conf
RUN rm -rf /snmpd/net-snmp-${SNMP_VERSION}*
RUN chmod +x /snmpd/snmpd.conf

EXPOSE 161 162

ENV TINI_VERSION v0.18.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini", "-vvv", "-g", "-w", "--"]

RUN groupadd -r snmp && useradd -r -g snmp snmp \
    && chown -R snmp /snmpd /tini && chgrp -R snmp /snmpd /tini
USER snmp

WORKDIR /snmpd

CMD ['/snmpd/sbin/snmpd', '-C', '-c', '/snmpd/snmpd.conf']

# NOTE: docker run -it --rm registry.cn-beijing.aliyuncs.com/xx-z/net-snmp:v1 /snmpd/snmpd -h
# docker ps -a | grep snmp | awk '{print $1}' | xargs docker stop | xargs docker rm