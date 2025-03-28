# generate-video-captions

Automated Video Caption Generator for Visually Impaired People

Our goal is to develop a web application that can effortlessly create descriptions for live video feeds captured by mobile cameras that helps visually impaired individuals to better assess their surroundings. The web application will take live video as input to produce descriptive audio captions that narrate the content of the scene.





## Dataset


We are utilizing the MVSD (Microsoft Research Video Description Corpus) dataset for this project. The dataset comprises 1,970 distinct videos, each accompanied by 80,827 unique captions. Multiple captions are associated with each video, a design choice made to accommodate the diverse ways a single video can be described. For instance, a video featuring a squirrel eating a peanut may be described in various ways, such as:

    1. a squirrel is eating a nut
    2. the squirrel is eating
    3. a chipmunk is eating some food
    4. the squirrel ate the peanut out of the shell etc....

This enables model to learn about different caption without processing lots of video.

Downloaded from : https://www.kaggle.com/datasets/vtrnanh/msvd-dataset-corpus https://www.kaggle.com/datasets/sarthakjain004/msvd-clips





## Pre-Processing

Videos are basically series of images. We don't know how to identify features of images, but we know how to identify features of an image. To do that, we will convert each video into multiple images. We have generated 80 different frames from videos, and we will identify features of each frame. We will store each feature as a numpy array. We have used the pre-trained model VGG16 from Keras to extract features from each image.

We have also processed the annotation file to make it easy to use in feature extraction.

We have performed feature extraction on an HPC cluster for each of the 1,980 images.


## Model training - To be done

After extracting the features, we will use an Encoder-Decoder model to generate captions. A stacked LSTM first encodes the frames one by one, taking as input the output of a Convolutional Neural Network (CNN) applied to each input frame's intensity values. Once all frames are read, the model generates a sentence word by word. The encoding and decoding of the frame and word representations are learned jointly from a parallel corpus. The videos are a sequence of frames. LSTM tends to work better with sequences; therefore, we will use LSTM for the encoder. We will feed the result of the encoder to the decoder, which will generate the text as output. We will use LSTM for the decoder as well.
## Test Model 

Before training the data, we will divide it into a training and testing dataset. The test dataset will be used to assess the accuracy of our model.
## Build Application 

We will build a user interface (UI) to allow users to input videos and generate audio captions.

## References

[1] Agarwal, L., Verma, B. From methods to datasets: A survey on Image-Caption Generators. Multimed Tools Appl (2023)

[2] N. Indumathi, R. J. Divyalakshmi, J. Stalin, V. Ramachandran and P. Rajaram, "Apply Deep Learning-based CNN and LSTM for Visual Image Caption Generator," 2023 3rd International Conference on Advance Computing and Innovative Technologies in Engineering (ICACITE), Greater Noida, India, 2023, pp. 1586-1591, doi: 10.1109/ICACITE57410.2023.10183097.

[3] A. Singh and D. Vij, "CNN-LSTM based Social Media Post Caption Generator," 2022 2nd International Conference on Innovative Practices in Technology and Management (ICIPTM), Gautam Buddha Nagar, India, 2022, pp. 205-209, doi: 10.1109/ICIPTM54933.2022.9754189.

[4] https://arxiv.org/abs/1505.00487?source=post_page-----511984a2cfff--------------------------------

[5]https://towardsdatascience.com/image-captioning-with-keras-teaching-computers-to-describe-pictures-c88a46a311b8
