import time
import cv2
import label_image
import os,random
import subprocess
import vlc
import pafy
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
size = 4

# let's load the xml
classifier = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
global text
webcam = cv2.VideoCapture(0)
now = time.time()
future = now + 60
while True:
    (rval, im) = webcam.read()
    im = cv2.flip(im, 1, 0)  # Flip to act as a mirror
    # Resize the image to speed up detection
    mini = cv2.resize(im, (int(im.shape[1] / size), int(im.shape[0] / size)))
    # detect MultiScale / faces
    faces = classifier.detectMultiScale(mini)
    # Draw rectangles around each face
    for f in faces:
        (x, y, w, h) = [v * size for v in f]  # Scale the shapesize backup
        sub_face = im[y:y + h, x:x + w]
        FaceFileName = "test.jpg"  # Saving the current image from the webcam for testing.
        cv2.imwrite(FaceFileName, sub_face)
        text = label_image.main(FaceFileName)  # Getting the Result from the label_image file, i.e., Classification Result.
        text = text.title()  # Title Case looks Stunning.
        font = cv2.FONT_HERSHEY_TRIPLEX

        if text == 'Angry':
            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 25, 255), 7)
            cv2.putText(im, text, (x + h, y), font, 1, (0, 25,255), 2)

        if text == 'Smile':
            cv2.rectangle(im, (x, y), (x + w, y + h), (0,260,0), 7)
            cv2.putText(im, text, (x + h, y), font, 1, (0,260,0), 2)

        if text == 'Fear':
            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 255), 7)
            cv2.putText(im, text, (x + h, y), font, 1, (0, 255, 255), 2)

        if text == 'Sad':
            cv2.rectangle(im, (x, y), (x + w, y + h), (0,191,255), 7)
            cv2.putText(im, text, (x + h, y), font, 1, (0,191,255), 2)

    # Show the image/
    cv2.imshow('Music player with Emotion recognition', im)
    key = cv2.waitKey(30)& 0xff
    if time.time() > future:##after 20second music will play
        try:
            cv2.destroyAllWindows()
            mp = 'C:/Program Files (x86)/Windows Media Player/wmplayer.exe'
            if text == 'Angry':
                AngryURL = "https://www.youtube.com/watch?v=FZLILV18ut8&list=PL_MH8gOS_ETiNT1NF8B46JYHZe6fXWfVW&index=6"
                video = pafy.new(AngryURL)
                best = video.getbest()
                playurl = best.url
                Instance = vlc.Instance()
                player = Instance.media_player_new()
                Media = Instance.media_new(playurl)
                Media.get_mrl()
                player.set_media(Media)
                player.play()
                # randomfile = random.choice(os.listdir("/home/eddie/Desktop/python/music_player_with_emotions/songs/Angry/"))
                # print('You are angry !!!! please calm down:) ,I will play song for you :' + randomfile)
                # file = ('/home/eddie/Desktop/python/music_player_with_emotions/songs/Angry/' + randomfile)
                # subprocess.call([mp, file])
            if text == 'Smile':
                SmileURL = "https://www.youtube.com/watch?v=vZA5heWazIQ"
                video = pafy.new(SmileURL)
                best = video.getbest()
                playurl = best.url
                Instance = vlc.Instance()
                player = Instance.media_player_new()
                Media = Instance.media_new(playurl)
                Media.get_mrl()
                player.set_media(Media)
                player.play()
                # randomfile = random.choice(os.listdir("/home/eddie/Desktop/python/music_player_with_emotions/songs/Smile/"))
                # print('You are smiling :) ,I playing special song for you: ' + randomfile)
                # file = ('/home/eddie/Desktop/python/music_player_with_emotions/songs/Smile/' + randomfile)
                # subprocess.call([mp, file])

            if text == 'Fear':
                FearURL = "https://www.youtube.com/watch?v=q-wGMlSuX_c"
                video = pafy.new(FearURL)
                best = video.getbest()
                playurl = best.url
                Instance = vlc.Instance()
                player = Instance.media_player_new()
                Media = Instance.media_new(playurl)
                Media.get_mrl()
                player.set_media(Media)
                player.play()
                # randomfile = random.choice(os.listdir("/home/eddie/Desktop/python/music_player_with_emotions/songs/songs/Fear/"))
                # print('You have fear of something ,I playing song for you: ' + randomfile)
                # file = ('/home/eddie/Desktop/python/music_player_with_emotions/songs/Fear/' + randomfile)
                # subprocess.call([mp, file])

            if text == 'Sad':
                FearURL = "https://www.youtube.com/watch?v=BZsXcc_tC-o"
                video = pafy.new(FearURL)
                best = video.getbest()
                playurl = best.url
                Instance = vlc.Instance()
                Sadplayer = Instance.media_player_new()
                Media = Instance.media_new(playurl)
                Media.get_mrl()
                Sadplayer.set_media(Media)
                Sadplayer.play()
                # randomfile = random.choice(os.listdir("/home/eddie/Desktop/python/music_player_with_emotions/songs/Sad/"))
                # print('You are sad,dont worry:) ,I playing song for you: ' + randomfile)
                # file = ('/home/eddie/Desktop/python/music_player_with_emotions/songs/Sad/' + randomfile)
                # subprocess.call([mp, file])
            break

        except :
            print('Please stay focus in Camera frame atleast 15 seconds & run again this program:)')
            break

    if key == 27:  # The Esc key
        break
