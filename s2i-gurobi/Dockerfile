FROM registry.access.redhat.com/ubi7/python-38

LABEL name="s2i-gurobi" \
      maintainer="koree@redhat.com" \
      vendor="Gurobi" \
      version="9.0.2" \
      summary="Gurobi solvers base image" \
      description="Base image with gurobi dependencies integrated due to lack of pip packages"

USER root

RUN yum upgrade -y && \
    yum repolist && \
    yum clean all

# install gurobi - this for you flor :)
ENV BIN_URL=https://packages.gurobi.com/9.0/gurobi9.0.2_linux64.tar.gz
ENV GUROBI_HOME=/opt/gurobi/linux64
ENV PATH=${PATH}:${GUROBI_HOME}/bin
ENV LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${GUROBI_HOME}/lib

RUN curl -k ${BIN_URL} | tar zxf - -C /opt && \
    mv /opt/gurobi902 /opt/gurobi && \
    cd ${GUROBI_HOME} && \
    python3 setup.py install

### Setup user for build execution and application runtime
ENV APP_ROOT=/opt/app-root
ENV PATH=${APP_ROOT}/bin:${PATH} HOME=${APP_ROOT}

COPY bin/ ${APP_ROOT}/bin/

RUN chmod -R u+x ${APP_ROOT}/bin && \
    chgrp -R 0 ${APP_ROOT} && \
    chmod -R g=u ${APP_ROOT} /etc/passwd

### Containers should NOT run as root as a good practice
USER 1001
WORKDIR ${APP_ROOT}

### user name recognition at runtime w/ an arbitrary uid - for OpenShift deployments
ENTRYPOINT [ "uid_entrypoint" ]

CMD [ "/opt/app-root/builder/run" ]