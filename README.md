# Distance Transform in Python

## Description

This repostiry contains the python code to reproduce the results described in the paper ["Distance Transforms of Sampled Functions"](http://cs.brown.edu/people/pfelzens/papers/dt-final.pdf)

All repository is based in the C++ code that you can find [here](http://cs.brown.edu/people/pfelzens/dt/)

## Dependences

Only use OpenCV and Numpy (The versions I've used are: opencv-python==3.4.1.15 and opencv-python==3.4.1.15)

## Usage

You need a **binary image** where the object respect you want to calculate de Distance Transform **must have the value 0** and the background any other value.

You must use the absolute paths for both input and output images (Including names and extensions of the images)

To run the script:

```
python create_dt.py --input_img path_to_original_binary_image --output_img path_to_desired_save_img
```
