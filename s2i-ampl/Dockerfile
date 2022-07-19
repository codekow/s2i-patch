FROM registry.access.redhat.com/ubi7/python-38

LABEL name="s2i-ampl" \
      maintainer="koree@redhat.com" \
      vendor="COIN-OR / AMPL" \
      summary="AMPL Open Source Tools" \
      description="Base image with AMPL dependencies integrated"

USER root

RUN yum upgrade -y && \
    yum repolist && \
    yum clean all

COPY bin/ /usr/local/bin/

# install AMPL tools
# See https://ampl.com/products/solvers/open-source
ENV BIN_URL=https://ampl.com/dl/open/ampl-open-linux64.zip

WORKDIR /usr/local/bin

RUN curl -L ${BIN_URL} -o install.zip && \
    unzip install.zip && \
    rm install.zip && \
    chmod -R u+x /usr/local/bin

RUN chmod -R u+x ${APP_ROOT}/bin && \
    chgrp -R 0 ${APP_ROOT} && \
    chmod -R g=u ${APP_ROOT} /etc/passwd

### Containers should NOT run as root as a good practice
USER 1001
WORKDIR ${APP_ROOT}

### user name recognition at runtime w/ an arbitrary uid - for OpenShift deployments
ENTRYPOINT [ "uid_entrypoint" ]

CMD [ "/opt/app-root/builder/run" ]