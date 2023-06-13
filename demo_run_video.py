from chain_video_processor import ChainVideoProcessor

if __name__ == '__main__':
    chain_processor = ChainVideoProcessor()
    chain_processor.init_with_plugins()

    chain_processor.run_video_chain("demo_video.mp4","demo_video_res.mp4", fps=25.0, threads=4,
                                    chain="blur,to_grayscale", video_audio="demo_video.mp4")
    # video_audio also copy audio stream from original file
    # can work without it

    chain_processor.is_demo_row_render = True
    chain_processor.run_video_chain("demo_video.mp4", "demo_video_res_row.mp4", fps=25.0, threads=4,
                                    chain="blur,to_grayscale", video_audio="demo_video.mp4")

    print("Video processing completed!")