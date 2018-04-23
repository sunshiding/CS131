# CS131 作业留存
My Solution to Homework of CS131 Computer Vision: Foundations and Applications

课程地址 http://vision.stanford.edu/teaching/cs131_fall1718/

课程讲义 https://github.com/StanfordVL/CS131_notes


## Homework0：Basics
Homework 0 sets up the course with an introduction on how to use images in python and numpy. 
It covers basic linear algebra that would be helpful through the course.

### Question 1: Linear Algebra Review
### Question 2: Image Manipulation

完成时间：2018.4.9


## Homework1：Filters - Instagram
Homework 1 starts off the topics in computer vision by understanding concepts such as convolutions, linear systems and different kernels and how to design them to find certains signals in images.

### Part 1: Convolution
### Part 2: Cross-Correlation
### Part 3: Separable Filter

完成时间：2018.4.12


## Homework2: Edges - Smart car lane detection
Homework 2 focuses on edge detection, applying it to lane detection to aid self driving cars.

### Part 1: Canny Edge Detector
1. Smoothing
2. Finding gradients
3. Non-maximum suppression
4. Double thresholding
5. Edge tracking by hysterisis
### Part 2: Lane Detection
1. Detect edges using the Canny edge detector.
2. Extract the edges in the region of interest (a triangle covering the bottom corners and the center of the image).
3. Run Hough transform to detect lanes.

完成时间：2018.4.15

## Homework3: Panorama-Image stitching
Homework 3 introduces SIFT and RANSAC, 
which are useful for finding corresponding points in multiple images, 
enabling applications like panorama creation, 
which is a common feature in most of our smart phones.

### Part 1 Harris Corner Detector
### Part 2 Describing and Matching Keypoints
### Part 3 Transformation Estimation
### Part 4 RANSAC
### Part 5 Histogram of Oriented Gradients (HOG) 