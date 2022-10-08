FROM python:3.7-slim-buster

WORKDIR /workspace/project

ENV GRADIO_SERVER_PORT 8080

EXPOSE 8080

COPY requirements.txt requirements.txt

RUN pip3 install --no-cache-dir -r requirements.txt\
    && rm -rf /root/cache/pip/*\
    && rm requirements.txt\
    && rm -rf /tmp/*

ENTRYPOINT python src/cifar10_demo_scripted.py ckpt_path=logs/train/runs/2022-10-07_22-38-18/model.script.pt