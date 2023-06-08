# Blur example filter
# author: Vladislav Janvarev

from chain_img_processor import ChainImgProcessor
import os

modname = os.path.basename(__file__)[:-3] # calculating modname

# start function
def start(core:ChainImgProcessor):
    manifest = { # plugin settings
        "name": "Blur filter", # name
        "version": "1.0", # version

        "default_options": {
            "power": 30,  #
        },

        "img_processor": {
            "blur": (init,process) # 1 function - init, 2 - process
        }
    }
    return manifest

def start_with_options(core:ChainImgProcessor, manifest:dict):
    pass

def init(core:ChainImgProcessor):
    import cv2
    pass

def process(core:ChainImgProcessor, img, params:dict):
    # params can be used to transfer some img info to next processors
    import cv2
    options = core.plugin_options(modname)

    ksize = (int(options["power"]), int(options["power"]))

    # Using cv2.blur() method
    image = cv2.blur(img, ksize)

    return image
