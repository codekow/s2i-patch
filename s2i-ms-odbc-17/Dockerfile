FROM registry.access.redhat.com/ubi7/python-38

LABEL name="s2i-ms-odbc-17" \
      maintainer="koree@redhat.com" \
      vendor="Microsoft" \
      version="17" \
      summary="Python s2i w/ Microsoft ODBC drivers" \
      description="Python base image patched with Microsoft ODBC drivers"

USER root

RUN curl https://packages.microsoft.com/keys/microsoft.asc > ./microsoft.asc &&\
    sha256sum ./microsoft.asc &&\
    rpm --import ./microsoft.asc
    # todo: verify signing key as this is blind trust

# NOTICE: kludges below
# see https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server
# see https://stackoverflow.com/questions/63262668/rhel-8-container-mssql-odbc-driver-e2fsprogs
# build speed up --disablerepo='*' --enablerepo='ubi*' --enablerepo='*microsoft*'

RUN rpm -Uvh https://packages.microsoft.com/config/rhel/7/packages-microsoft-prod.rpm && \
    yum remove unixODBC-utf16 unixODBC-utf16-devel && \
    yumdownloader --disablerepo='*' --enablerepo='ubi*' --enablerepo='*microsoft*' msodbcsql17 mssql-tools unixODBC unixODBC-devel && \
    ACCEPT_EULA=Y rpm -Uvh --nodeps *x86_64.rpm && \
    rm *.rpm && \
    yum clean all

# kludge to fix poor install
RUN cat /etc/odbcinst.ini > /etc/odbc.ini 

ENV PATH=$PATH:/opt/mssql-tools/bin

ADD odbc-test.py .

USER 1001
