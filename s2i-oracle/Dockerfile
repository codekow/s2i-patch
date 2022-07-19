FROM registry.access.redhat.com/ubi7/python-38

LABEL name="s2i-ms-odbc-13" \
      maintainer="koree@redhat.com" \
      vendor="Oracle" \
      summary="Python s2i w/ Oracle ODBC drivers" \
      description="Python base image patched with Oracle ODBC drivers"

USER root

ARG ORACLE_FINGERPRINT='4214 4123 FECF C55B 9086  313D 72F9 7B74 EC55 1F03'
RUN curl -sL https://yum.oracle.com/RPM-GPG-KEY-oracle-ol7 -o /etc/pki/rpm-gpg/RPM-GPG-KEY-oracle && \
    gpg --quiet --with-fingerprint /etc/pki/rpm-gpg/RPM-GPG-KEY-oracle 2>/dev/null | grep "${ORACLE_FINGERPRINT}" && \
    rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-oracle && \
    rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release

# Internal URLs
# ARG ORACLE_BASIC_URL=https://files.apphn.ocp.na.xom.com/oracle/oracle-instantclient19.6-basic-19.6.0.0.0-1.x86_64.rpm
# ARG ORACLE_ODBC_URL=https://files.apphn.ocp.na.xom.com/oracle/oracle-instantclient19.6-odbc-19.6.0.0.0-1.x86_64.rpm

# ARG ORACLE_BASICLITE_URL=https://download.oracle.com/otn_software/linux/instantclient/19600/oracle-instantclient19.6-basiclite-19.6.0.0.0-1.x86_64.rpm
ARG ORACLE_BASIC_URL=https://download.oracle.com/otn_software/linux/instantclient/19600/oracle-instantclient19.6-basic-19.6.0.0.0-1.x86_64.rpm
ARG ORACLE_ODBC_URL=https://download.oracle.com/otn_software/linux/instantclient/19600/oracle-instantclient19.6-odbc-19.6.0.0.0-1.x86_64.rpm

RUN yum -y install unixODBC unixODBC-devel libaio && \
    yum -y install ${ORACLE_BASIC_URL} ${ORACLE_ODBC_URL} && \
    yum clean all

RUN echo '/usr/lib/oracle/19.6/client64/lib' > \
    /etc/ld.so.conf.d/oracle-instantclient.conf && \
    ldconfig

# install python packages
RUN pip install pyodbc==4.0.30 cx_Oracle==8.0.0

# add path info for TNS_ADMIN
ENV PATH=$PATH:/usr/lib/oracle/19.6/client64/bin
ENV TNS_ADMIN=/usr/lib/oracle/19.6/client64/network/admin

RUN mkdir -p ${TNS_ADMIN} && \
    chgrp -R 0 ${TNS_ADMIN} && \
    chmod -R g+rw ${TNS_ADMIN}

USER 1001