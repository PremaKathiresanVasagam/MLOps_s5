import pyrootutils

root = pyrootutils.setup_root(
    search_from=__file__,
    indicator=[".git", "pyproject.toml"],
    pythonpath=True,
    dotenv=True,
)

from typing import List, Tuple

import urllib

import numpy as np
from PIL import Image
from timm.data import resolve_data_config
from timm.data.transforms_factory import create_transform
import torch
import hydra
import gradio as gr
from omegaconf import DictConfig

from src import utils

log = utils.get_pylogger(__name__)

def demo(cfg: DictConfig) -> Tuple[dict, dict]:
    """Demo function.
    Args:
        cfg (DictConfig): Configuration composed by Hydra.

    Returns:
        Tuple[dict, dict]: Dict with metrics and dict with all instantiated objects.
    """

    assert cfg.ckpt_path

    log.info("Running Demo")

    log.info(f"Instantiating scripted model <{cfg.ckpt_path}>")
    model = torch.jit.load(cfg.ckpt_path)

    log.info(f"Loaded Model: {model}")

    classes=['airplane', 'automobile', 'bird', 'cat', 'deer',
           'dog', 'frog', 'horse', 'ship', 'truck']

    def predict_cifar10_images(image):
        if image is None:
            return None
        config = resolve_data_config({}, model=model)
        transform = create_transform(**config)

        img_tensor = transform(image).unsqueeze(0)  # transform and add batch dimension
        
        preds = model.forward_jit(img_tensor)

        preds = preds[0].tolist()
        label_pred = {classes[i]: preds[i] for i in range(10)}

        return label_pred

    demo = gr.Interface(
        fn=predict_cifar10_images,
        inputs=gr.Image(type='pil'),
        outputs=gr.Label(num_top_classes=10),
    )
    demo.launch(server_name="0.0.0.0", share=True)

@hydra.main(
    version_base="1.2", config_path=root / "configs", config_name="cifar10_demo_scripted.yaml"
)
def main(cfg: DictConfig) -> None:
    demo(cfg)

if __name__ == "__main__":
    main()