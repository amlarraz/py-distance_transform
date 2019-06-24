import argparse
import cv2

from dt import *

def get_arguments():
    parser = argparse.ArgumentParser(description="Faster and deeplabv2 inference.")
    #Arguments for both inferences:
    parser.add_argument("--input_img", type=str, default=None,
                        help="Path to the image from which you want to calculate the distance transform")
    parser.add_argument("--output_img", type=str, default=None,
                        help="Path and name of the image where you want to save the result")
    return parser.parse_args()

def main():
    args = get_arguments()
    print(args.input_img, args.output_img)
    img = cv2.imread(args.input_img, 0)
    out = dt_img_bin(img.astype(np.float64))
    gray = to_grayscale(out)  # Values between 0-255
    if args.output_img is not None:
        cv2.imwrite(args.output_img, gray)
	return None

if __name__ == "__main__":
    main() 
