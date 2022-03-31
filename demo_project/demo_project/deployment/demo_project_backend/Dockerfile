FROM python:3.7 as base

# TODO: подставьте свои репозитории
# COPY ./deployment/apt/apt.conf /etc/apt/apt.conf
# COPY ./deployment/apt/sources.list /etc/apt/sources.list


WORKDIR /app

# ====================================================
FROM base as demo_project_backend-build

ENV PIP_CONFIG_FILE=/app/pip.conf
ENV USERNAME=app
ENV PATH=$PATH:/opt/bin

RUN groupadd -r $USERNAME && \
    useradd -r -g $USERNAME -d /home/$USERNAME -s /sbin/nologin -c "Docker image user" app

COPY ./deployment/demo_project_backend/entrypoint_*.sh /usr/bin/

# TODO: подставьте свой pip.conf
COPY ./deployment/demo_project_backend/pip.conf /app/pip.conf
RUN chmod +x /usr/bin/entrypoint_*.sh

COPY ./components/demo_project_backend /app
RUN pip install --upgrade --no-cache-dir pip && \
    pip install --no-cache-dir . && \
    python setup.py bdist_wheel && \
    rm -fr /app/pip.conf

WORKDIR /usr/local/lib/python3.7/site-packages/

USER $USERNAME

# ====================================================
FROM demo_project_backend-build as demo_project_backend-tests

ENV PIP_CONFIG_FILE=/app/pip.conf
USER root
WORKDIR /app
WORKDIR /app
# TODO: подставьте свой pip.conf
COPY ./deployment/demo_project_backend/pip.conf /app/pip.conf

RUN pip install --no-cache-dir -e .[dev] && \
    pytest ./tests/unit && \
    pytest ./tests/integration && \
    rm -fr /app/pip.conf

# ====================================================
FROM demo_project_backend-build as demo_project_backend-final
