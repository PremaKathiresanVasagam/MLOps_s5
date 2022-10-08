# EMLO V2 - Session 02

## 02 - Pytorch lightning with timm model and cifar10 datatset - Docker creation

## Steps:

#### Created and tested in gitpod - https://www.gitpod.io/ 

1. Use the pytorch lightning model template from https://github.com/ashleve/lightning-hydra-template.git for updating the cifar10 dataset and timm model.
2. Create model->timm.yaml with configurable parameter model = (resnet, efficient_b0, ...), and everytime to check the results for different models model parameter needs to be updated.
3. Create models->timm_module.py and update the class_name, lightning module parameter passed and timm.yaml in the cfg of main function.
4. Create an experiment: experiment-> cifar10_exp.yaml and update the defaults with cifar10 datatset and timm model. And update the model net parameters with model_name, pretrained values, num_classes.
5. Update the requirements.txt file with the needed package of torch and torchvision - cpu version to reduce the docker filesize.
6. Dockerfile creation: 
    a. Usage of alpine or slim images - used slim here to reduce size. 
    b. *To reduce the image size, use the CPU version of torch & torchvision packages. (reduces to 1.09GB from 2.5GB) *
    c. Remove the cache and requirements.txt after installing the packages.
7. Update the makefile with docker build. Build docker image using docker build --tag <imagename>.
8. Now docker run using docke run --it -v `pwd`: workspace/project <imagename> bash to mount the host in the docker container. This step is essential when logs are generated it is usually within the docker container, when we mount, it gets saved in the host system as well.
9. Now python3 src/train.py and it automatically evaluates as well since it is a pretrained model.


# MLOps_s4
