# CPD-Dataset
Computer Printed Digits dataset

## Overview
This is a simple dataset of the digits 0-9 how they are displayed on your computer screen.

![0](https://github.com/christianpfister43/CPD-Dataset/blob/main/data/example_images/digit_image0.png)
![1](https://github.com/christianpfister43/CPD-Dataset/blob/main/data/example_images/digit_image1.png)
![2](https://github.com/christianpfister43/CPD-Dataset/blob/main/data/example_images/digit_image2.png)
![3](https://github.com/christianpfister43/CPD-Dataset/blob/main/data/example_images/digit_image3.png)
![4](https://github.com/christianpfister43/CPD-Dataset/blob/main/data/example_images/digit_image4.png)
![5](https://github.com/christianpfister43/CPD-Dataset/blob/main/data/example_images/digit_image5.png)
![6](https://github.com/christianpfister43/CPD-Dataset/blob/main/data/example_images/digit_image6.png)
![7](https://github.com/christianpfister43/CPD-Dataset/blob/main/data/example_images/digit_image7.png)
![8](https://github.com/christianpfister43/CPD-Dataset/blob/main/data/example_images/digit_image8.png)
![9](https://github.com/christianpfister43/CPD-Dataset/blob/main/data/example_images/digit_image9.png)

It is in the style of the MNIST dataset of hand written digits. All digits are 28 * 28 pixels.


## How to get the Dataset
You can  donwload the dataset that I created from my [google drive](https://drive.google.com/drive/folders/1leyxPGTM2nPgeGwlaY4eg0ndbuB7Z3ad?usp=sharing):

This contain 17700 images of various font-styles and shades of gray in the background and the correspondig labels.

## How to create your own custom dataset
### Prerequisites
please install the required python packages: `pip install -r requirements.txt` 


If the labels file (`label.csv`) is already present, the new round of data will be appended

### General Usage:

Use the pre-defined numbers.ods (Apache Open Office) to display the numbers on your screen (I recommend to use 2 screens) and run the `create_dataset.py` script from your second screen in a terminal: `python create_dataset.py`
Depending on your Screen and its resolution (1920x1080) you might need to fine-tune the parameters in the script for height/ width and the sliding image window.

The default `numbers.ods` consists of 15 columns with 10 rows (with a digit 0-9). 

**The script will take screenshots of each number diplayed and save them under the specified `save_path`.** 

After each run, change the font-type (and maybe background) in the `numbers.ods` and run the script again. The new images will be saved in the `data/images` and the labels.csv will be appended in each run.

Repeat these steps untill you have enough data.




