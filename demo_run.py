import cv2
from chain_img_processor import ChainImgProcessor

if __name__ == '__main__':
    chain_processor = ChainImgProcessor()
    chain_processor.init_with_plugins()

    img = cv2.imread("demo_photo.jpg")
    resimg, params = chain_processor.run_chain(img, {}, "blur,to_grayscale")
    cv2.imwrite("demo_photo_res.jpg", resimg)

    chain_processor.is_demo_row_render = True
    resimg, params = chain_processor.run_chain(img, {}, "blur,to_grayscale")
    cv2.imwrite("demo_photo_res_row.jpg", resimg)

    print("Chain completed!")