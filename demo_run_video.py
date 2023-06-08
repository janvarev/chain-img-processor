from chain_video_processor import ChainVideoProcessor

if __name__ == '__main__':
    chain_processor = ChainVideoProcessor()
    chain_processor.init_with_plugins()

    chain_processor.run_video_chain("demo_video.mp4","demo_video_res.mp4", 25.0, 4, "blur") # grayscale affects RGB format, so we don't use it

    print("Video processing completed!")