FROM python:3.7-slim-buster

WORKDIR /workspace/project

ENV GRADIO_SERVER_PORT 80

EXPOSE 80

ADD src/utils src/utils

ADD configs configs

COPY ["*.toml","src/cifar10_demo_scripted.py","requirements.txt" ,"requirements.txt" ,"./"]

RUN pip3 install --no-cache-dir -r requirements.txt\
    && rm -rf /root/cache/pip/*\
    && rm requirements.txt\
    && rm -rf /tmp/*

ENTRYPOINT python3 cifar10_demo_scripted.py
