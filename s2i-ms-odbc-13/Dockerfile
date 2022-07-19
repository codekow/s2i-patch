FROM registry.access.redhat.com/ubi7/python-38

LABEL name="s2i-ms-odbc-13" \
      maintainer="koree@redhat.com" \
      vendor="Microsoft" \
      version="13" \
      summary="Python s2i w/ Microsoft ODBC drivers" \
      description="Python base image patched with Microsoft ODBC drivers"

USER root

RUN curl https://packages.microsoft.com/keys/microsoft.asc > ./microsoft.asc &&\
    sha256sum ./microsoft.asc &&\
    rpm --import ./microsoft.asc
    # todo: verify signing key as this is blind trust

# see https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server
# build speed up --disablerepo='*' --enablerepo='ubi*' --enablerepo='*microsoft*'
RUN rpm -Uvh https://packages.microsoft.com/config/rhel/7/packages-microsoft-prod.rpm && \
    yum remove unixODBC-utf16 unixODBC-utf16-devel && \
    ACCEPT_EULA=Y yum -y --setopt=tsflags=nodocs install msodbcsql-13.0.1.0-1 mssql-tools-14.0.2.0-1 && \
    yum clean all 

# kludge to fix poor install
RUN cat /etc/odbcinst.ini > /etc/odbc.ini 

ENV PATH=$PATH:/opt/mssql-tools/bin

USER 1001
