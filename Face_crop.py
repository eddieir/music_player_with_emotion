import cv2
import glob

images = glob.glob("*.jpg")

for image in images:
    facedata = "haarcascade_frontalface_alt.xml"
    casecade = cv2.CascadeClassifier(facedata)
    img = cv2.imread(image,0)

    re=cv2.resize(img,(int(img.shape[1]),int(img.shape[0])))
    faces = casecade.detectMultiScale(re)

    for f in faces:
        x,y,w,h = [v for v in f]
        Rect = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        sub_face = img[y:y+h,x:x+w]

        f_name = image.split('/')
        f_name = f_name[-1]
        cv2.imshow("Checking",sub_face)
        cv2.waitKey(500)
        cv2.destroyWindow()

        cv2.imwrite("resized_"+image,sub_face)