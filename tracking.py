# import the necessary packages
import numpy as np
import cv2
import argparse
from DBHandler import DBHandler

def main(room, building):
    url = 'http://192.168.111.63:8080/video'

    db = DBHandler()
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    cv2.startWindowThread()

    cap = cv2.VideoCapture(url)
    count = 0
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # resizing for faster detection
        frame = cv2.resize(frame, (640, 480))
        # using a greyscale picture, also for faster detection
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

        # detect people in the image
        # returns the bounding boxes for the detected objects
        boxes, weights = hog.detectMultiScale(frame, winStride=(8,8) )

        boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])

        for (xA, yA, xB, yB) in boxes:
            # display the detected boxes in the colour picture
            cv2.rectangle(frame, (xA, yA), (xB, yB),
                            (0, 255, 0), 2)
        
        if count % 1000 == 0:
            db.update_room(building, room, len(boxes))

        cv2.imshow('frame',frame)
        count += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()

    # finally, close the window
    cv2.destroyAllWindows()
    cv2.waitKey(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='tracking')
    parser.add_argument('--room', metavar='id', required=True,
                        help='the room id')
    parser.add_argument('--building', metavar='id', required=True,
                        help='the building code')
    args = parser.parse_args()
    main(room=args.room, building=args.building)