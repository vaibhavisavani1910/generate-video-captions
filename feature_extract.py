import numpy as np
import shutil
import tqdm
import os
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.models import Model
import cv2

#   This file is used to extract features from video. Video is basically searies of pictures. We will convert the video 
#   into series of images. Next step is to store that images.
#   We will store 80 frames from video and then use The VGG16 from keras is used to extract features from those images
#   We will store those features as numpy array and store them into "extraced_features" folder for each videos.
#   Then we will use these features to train our encoder decoder model to generate caption

def model_extract(video, model, base_path):
    
    if os.path.exists(base_path + 'tmp'): 
        shutil.rmtree(base_path)
        
    id = video.split(".")[0]
    print(id)
    print(f'Processing video {video}')

    # convert videos into images
    os.makedirs(base_path + 'tmp')

    video_capture = cv2.VideoCapture(os.path.join(base_path, 'video', video))
    frames = []
    for count, (result, image) in iter(lambda: video_capture.read(), (False, None)):
        if not result:
            break

        frames.append(os.path.join(base_path, 'img%d.jpg'% count))
        cv2.imwrite(os.path.join(base_path, 'img%d.jpg'% count) , image)
    
    video_capture.release()
    cv2.destroyAllWindows()
    peoccesed = np.round(np.linspace(0, len(frames) - 1, 80))
    sampled_frames = []
    for process in peoccesed:
        sampled_frames.append(frames[int(process)])
    images = np.zeros((len(sampled_frames), 224, 224, 3))

    i = 0
    while i < len(sampled_frames):
        img = cv2.imread(os.path.join(base_path, 'img%d.jpg'% i))
        img = cv2.resize(img, (224, 224))
        images[i] = img
        i += 1

    processed_frames = np.array(processed_frames)
    model_predictions = model.predict(processed_frames, batch_size=128)
    image_features = np.array(model_predictions)
    shutil.rmtree(os.path.join(base_path, 'tmp'))

    return image_features



if __name__ == "__main__":
    
    # Load VGG16 model with imagenet weights
    base_model = VGG16(weights="imagenet", include_top=True, input_shape=(224, 224, 3))
    model = Model(inputs=base_model.input, outputs=base_model.layers[-2].output)
    
    if not os.path.isdir(os.path.join('data','training_data', 'extracted_feature')):
        os.mkdir(os.path.join('data','training_data', 'extracted_feature'))

    videos = os.listdir(os.path.join('data','training_data', 'video'))

    for video in videos:
        if video.endswith('.avi'):
            feature_npy = os.path.join('data','training_data', 'extracted_feature', video + '.npy')
            features = model_extract(video, model,os.path.join('data','training_data'))
            np.save(feature_npy, features)