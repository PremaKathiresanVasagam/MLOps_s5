


<div align="center">

# Project Name - Gradio Demo for CIFAR10 model using scripted model

<a href="https://pytorch.org/get-started/locally/"><img alt="PyTorch" src="https://img.shields.io/badge/PyTorch-ee4c2c?logo=pytorch&logoColor=white"></a>
<a href="https://pytorchlightning.ai/"><img alt="Lightning" src="https://img.shields.io/badge/-Lightning-792ee5?logo=pytorchlightning&logoColor=white"></a>
<a href="https://hydra.cc/"><img alt="Config: Hydra" src="https://img.shields.io/badge/Config-Hydra-89b8cd"></a>
<a href="https://github.com/ashleve/lightning-hydra-template"><img alt="Template" src="https://img.shields.io/badge/-Lightning--Hydra--Template-017F2F?style=flat&logo=github&labelColor=gray"></a><br>
[![Paper](http://img.shields.io/badge/paper-arxiv.1001.2234-B31B1B.svg)](https://www.nature.com/articles/nature14539)
[![Conference](http://img.shields.io/badge/AnyConference-year-4b44ce.svg)](https://papers.nips.cc/paper/2020)

</div>
## Description


# EMLO V4 - Session 04

## 04 - Gradio Demo for CIFAR10 model using scripted model

## Steps:

#### Created and tested in gitpod - https://www.gitpod.io/ 

### Steps to run this repo using docker - makefile:

1. make docker-build or docker build --tag s4_gradio_demo .
2. make docker-portmap (port 8080 is mapped to public gradio url) or docker run -t -p 8080:8080 s4_gradio_demo:latest

### Updates made
1. Add forward_jit(image) to src/models/timm_module.py
2. create cifar10_demo_scripted.py file by importing timm packages, adding classes of cifar10 to alist/dictionary, and a function to predict images, update config file with cifar10_demo_scripted.yaml, change input image type to "pil" in gradio interface.

# MLOps_s4
