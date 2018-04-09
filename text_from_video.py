from PIL import Image
import pytesseract
import cv2
import sys

video_capture = cv2.VideoCapture(0)

def start_capture():
<<<<<<< HEAD
<<<<<<< HEAD
    while True:
=======

    while True:

>>>>>>> parent of 0a13601... Revert "TextFromImageOrVideoCommit"
=======
    while True:
>>>>>>> init commit
        if not video_capture.isOpened():
            print('Unable to load camera.')
            sleep(5)
            pass
<<<<<<< HEAD
<<<<<<< HEAD
        # Capture frame-by-frame
        ret, frame = video_capture.read()
        #extracting Text from curent frame
=======

        # Capture frame-by-frame
        ret, frame = video_capture.read()
>>>>>>> parent of 0a13601... Revert "TextFromImageOrVideoCommit"
=======
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        #extracting Text from curent frame
>>>>>>> init commit
        text = pytesseract.image_to_string(frame, lang = 'eng')

        if len(text) > 0:
            #text = pytesseract.image_to_string(im)
            print("Text Detect:\n "+text)

        # Display the resulting frame
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()

<<<<<<< HEAD
    print("End")
=======
    print("Vido End")
>>>>>>> init commit

start_capture()
