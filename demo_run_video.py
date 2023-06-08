from chain_video_processor import ChainVideoProcessor

if __name__ == '__main__':
    chain_processor = ChainVideoProcessor()
    chain_processor.init_with_plugins()

    chain_processor.run_video_chain("demo_video.mp4","demo_video_res.mp4", fps=25.0, threads=4, chain="blur") # grayscale affects RGB format, so we don't use it

    print("Video processing completed!")