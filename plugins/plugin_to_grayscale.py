# To grayscale example filter
# author: Vladislav Janvarev

from chain_img_processor import ChainImgProcessor
import os

modname = os.path.basename(__file__)[:-3] # calculating modname

# start function
def start(core:ChainImgProcessor):
    manifest = { # plugin settings
        "name": "Gray scale filter", # name
        "version": "1.0", # version

        "img_processor": {
            "to_grayscale": (init,process) # 1 function - init, 2 - process
        }
    }
    return manifest


def init(core:ChainImgProcessor):
    import cv2
    pass

def process(core:ChainImgProcessor, img, params:dict):
    # params can be used to transfer some img info to next processors
    import cv2
    options = core.plugin_options(modname)

    image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    return image
