# chain-img-processor
Chain IMG processor framework with plugins for neuronet pipelines etc.

You can run pipeline of image transformations with this processor. Also, you can use it as base framework for your own image transformation software. 

Concrete transformation is described as separate plugin, and easy to add or remove. Plugins/transformations can have their own user options (located in options folder)

Also included chain_video_processer (in BETA phase), that convert videos applying chain to each frame **WITH MULTITHREADING**!

List of additional plugins here:
https://github.com/janvarev/chain-img-processor/issues/1
- Codeformer plugin for image/face upscaling/restore
- Example plugins
  - blur
  - to_grayscale
  - resize

## Example 

![origin](/demo_photo.jpg "origin photo")

Code (in demo_run.py)
```python
chain_processor = ChainImgProcessor()
chain_processor.init_with_plugins()

img = cv2.imread("demo_photo.jpg")
resimg, params = chain_processor.run_chain(img, {}, "blur,to_grayscale")
cv2.imwrite("demo_photo_res.jpg", resimg)
```

Result:

![result](/demo_photo_res.jpg "result photo")

If you set param `chain_processor.is_demo_row_render = True` you can get phases of image transformation (warning: work only on cv2 images, and on images the same size)

This is also can be applied to VIDEO processing too!

Example:
![result](/demo_photo_res_row.jpg "result row photo")


### More plugins

Please, post your additional plugins here:
https://github.com/janvarev/chain-img-processor/issues/1

## Plugin support

Plugins supported throw [Jaa.py](https://github.com/janvarev/jaapy) - minimalistic one-file plugin engine.

Plugins are located in the plugins folder and must start with the "plugins_" prefix.

Plugin settings, if any, are located in the "options" folder (created after the first launch).

Examples can be found in `plugins` dir.

Example plugin with options: plugin_blur.py

Example plugin without options: plugin_to_grayscale.py

## Specific plugin processing

Plugin can pass some details to next phase in chain, using `params` dict, that are specific for concrete img. 

As an example: `params["is_face"]` can share info was face detected on img, or not.

## Core options description (core.json)

Located in `options/core.json` after first run.

```python
{
    "default_chain": "blur,to_grayscale", # default chain to run
    "init_on_start": "blur,to_grayscale", # init these processors on start
},
```

## chain_video_processor

Descendant of ChainImgProcessor. Allow you to process whole video file.

IN BETA PHASE, some stuff may be unoptimal and is a subject to change.

Example in `demo_run_video.py`

Details:
- you need ffmpeg to be installed
- you need fps to be set during call
- audio will not be passed, you need to add it manually
- multithreads processing available (through Threads)
- for multithreads original code thanks https://github.com/RichardErkhov
- video save params can be adjusted in ffmpeg_writer.py file.

Example code:
```python
chain_processor = ChainVideoProcessor()
chain_processor.init_with_plugins()

chain_processor.run_video_chain("demo_video.mp4","demo_video_res.mp4", fps=25.0, threads=4, chain="blur") # grayscale affects RGB format, so we don't use it
```

Example of use row render:
<video src='https://github.com/janvarev/chain-img-processor/assets/18393788/9be8981a-db3b-4b01-a541-b98df12b61dd' />


## Credits
- Demo photo from Christopher Campbell https://unsplash.com/photos/rDEOVtE7vOs under Unsplash License
- Multithreads video original code thanks https://github.com/RichardErkhov
- FFMPEG_Writer original code licensed under MIT from Zulko (moviepy project) https://github.com/Zulko/moviepy/blob/master/moviepy/video/io/ffmpeg_writer.py
