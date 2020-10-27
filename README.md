This repo is dedicated to music player which is working base on the emotion of the person, 

Code Requirements

    Tensorflow
    Pafy
    vlc
    Expression: Could taken as the image from the webcame or could be taken as the image from the internet 
   
    
Steps need to follow for running the code:

Create Images folder with following subfolders:Angry,Happy,Sad in the project work space,
Once you created Image folder you need to put Face_crop.py & haarcascade_frontalface_alt.xml in every type of image folder, for example you put the code at Angry image folder and it will detect faces from images and convert it to the grayscale and make a new images in the same folder.
After that you can use the following code for training the model:  python3 retrain.py --output_graph=retrained_graph.pb --output_labels=retrained_labels.txt --architecture=MobileNet_1.0_224 --image_dir=images
And the last stage will be run the main code which is music_player.py



