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
--with-logfile=/var/log/snmpd.log \
--with-persistent-directory=${INSTALL_PATH}/var/net-snmp && make && make install

RUN ln -sn ${INSTALL_PATH}/sbin/snmpd /usr/bin/snmpd
RUN ln -sn ${INSTALL_PATH}/sbin/snmptrapd /usr/bin/snmptrapd
RUN cp ${INSTALL_PATH}/net-snmp-${SNMP_VERSION}/EXAMPLE.conf ${INSTALL_PATH}/snmpd.conf
RUN rm -rf ${INSTALL_PATH}/net-snmp-${SNMP_VERSION}*

RUN chmod +x ${INSTALL_PATH}/snmpd.conf

WORKDIR ${INSTALL_PATH}/bin/

COPY entrypoint.sh /usr/local/bin/
RUN chmod -R 777 /usr/local/bin/entrypoint.sh

RUN groupadd -r snmp && useradd -r -g snmp snmp \
    && chown -R snmp ${INSTALL_PATH} && chgrp -R snmp ${INSTALL_PATH}

USER snmp
EXPOSE 161 162

ENTRYPOINT ['entrypoint.sh']
CMD ['${INSTALL_PATH}/sbin/snmpd', '-h']
