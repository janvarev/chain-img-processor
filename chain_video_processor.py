from threading import Thread

from chain_img_processor import ChainImgProcessor,version

from termcolor import colored, cprint


from typing import Any

#version = "1.0.0"

class ThreadWithReturnValue(Thread):

    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args,
                                        **self._kwargs)

    def join(self, *args):
        Thread.join(self, *args)
        return self._return


# in beta
class ChainVideoProcessor(ChainImgProcessor):
    def __init__(self):
        ChainImgProcessor.__init__(self)

    def run_video_chain(self, source_video, target_video, fps, threads:int = 1, chain = None, params_frame_gen_func = None):
        import cv2
        from tqdm import tqdm
        from ffmpeg_writer import FFMPEG_VideoWriter # ffmpeg install needed

        cap = cv2.VideoCapture(source_video)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        temp = []
        with FFMPEG_VideoWriter(target_video, (width, height), fps) as output_video_ff:
            with tqdm(total=frame_count, desc='Processing', unit="frame", dynamic_ncols=True,
                      bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}{postfix}]') as progress:
                while True:
                    # getting frame
                    ret, frame = cap.read()
                    if not ret:
                        break

                    # we are having an array of length %gpu_threads%, running in parallel
                    # so if array is equal or longer than gpu threads, waiting
                    while len(temp) >= threads:
                        # we are order dependent, so we are forced to wait for first element to finish. When finished removing thread from the list
                        frame_processed, params = temp.pop(0).join()
                        # writing into output
                        output_video_ff.write_frame(frame_processed)
                        # updating the status
                        progress.update(1)

                    # calc params for frame
                    if params_frame_gen_func is not None:
                        params = params_frame_gen_func(self,frame)
                    else:
                        params = {}

                    # adding new frame to the list and starting it
                    temp.append(
                        ThreadWithReturnValue(target=self.run_chain, args=(frame, {}, chain)))
                    temp[-1].start()

                while len(temp) > 0:
                    # we are order dependent, so we are forced to wait for first element to finish. When finished removing thread from the list
                    frame_processed, params = temp.pop(0).join()
                    # writing into output
                    output_video_ff.write_frame(frame_processed)

                    progress.update(1)
