FROM centos:7
MAINTAINER actanble <actanble@gmail.com>

USER root

# Add APT Source
RUN yum install yum-fastestmirror -y
RUN yum -y install locales gcc make wget perl perl-devel file
RUN localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8

ENV SNMP_MODE agent

ARG SNMP_VERSION=5.8
ARG INSTALL_PATH=/snmpd

RUN mkdir -p ${INSTALL_PATH}
WORKDIR ${INSTALL_PATH}

RUN wget https://nchc.dl.sourceforge.net/project/net-snmp/net-snmp/${SNMP_VERSION}/net-snmp-${SNMP_VERSION}.tar.gz && \
tar zxvf net-snmp-${SNMP_VERSION}.tar.gz && \
cd net-snmp-${SNMP_VERSION} && \
./configure --prefix=${INSTALL_PATH} \
--enable-mfd-rewrites \
--with-default-snmp-version=2 \
--with-sys-contact=actanble@gmail.com \
--with-sys-location=China \
--with-logfile=${INSTALL_PATH}/var/snmpd.log \
--with-persistent-directory=${INSTALL_PATH}/var/net-snmp && make && make install

RUN ln -sn ${INSTALL_PATH}/sbin/snmpd /usr/bin/snmpd && ln -sn ${INSTALL_PATH}/sbin/snmptrapd /usr/bin/snmptrapd

RUN cp ${INSTALL_PATH}/net-snmp-${SNMP_VERSION}/EXAMPLE.conf ${INSTALL_PATH}/snmpd.conf
RUN rm -rf ${INSTALL_PATH}/net-snmp-${SNMP_VERSION}*
RUN chmod +x ${INSTALL_PATH}/snmpd.conf

EXPOSE 161 162

ENV TINI_VERSION v0.18.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini", "--"]

RUN groupadd -r snmp && useradd -r -g snmp snmp \
    && chown -R snmp ${INSTALL_PATH} /tini && chgrp -R snmp ${INSTALL_PATH} /tini
USER snmp

WORKDIR ${INSTALL_PATH}
CMD ['snmpd', './snmpd.conf']
## docker run -it --rm registry.cn-beijing.aliyuncs.com/xx-z/net-snmp:v1 /snmpd/snmpd -h