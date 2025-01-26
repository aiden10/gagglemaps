# import the necessary packages
import numpy as np
import cv2
import argparse
from DBHandler import DBHandler
import sounddevice as sd
import threading
import speech_recognition as sr 

def main(room, building, container):
    room_id = building + room
    url = 'http://192.168.111.63:8080/video'

    db = DBHandler()

    r = sr.Recognizer()

    def record_audio():
        while True:
            with sr.Microphone() as source:
                text = ''
                try:
                    audio_listened = r.listen(source, phrase_time_limit=10)
                    text = r.recognize_google(audio_listened)
                except Exception as e:
                    print('No words detected')
                if text == '':
                    continue
                if room_id in container.audio:
                    container.audio[room_id] = text
                else:
                    container.audio.update({room_id: text})

    def record_video():

        hog = cv2.HOGDescriptor()
        hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

        cv2.startWindowThread()

        # cap = cv2.VideoCapture(url)
        cap = cv2.VideoCapture(0)
        count = 0
        while(True):
            # Capture frame-by-frame
            ret, frame = cap.read()

            frame = cv2.resize(frame, (640, 480))
            frame_without_border = frame
            gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

            # detect people in the image
            boxes, weights = hog.detectMultiScale(frame, winStride=(8,8) )

            boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])

            for (xA, yA, xB, yB) in boxes:
                cv2.rectangle(frame, (xA, yA), (xB, yB),
                                (0, 255, 0), 2)
            
            if count % 100 == 0:
                db.update_room(building, room, len(boxes))
                if room_id in container.image:
                    container.image[room_id] = frame_without_border
                else:
                    container.image.update({room_id: frame_without_border})
            # print(f'Count: {count}, {len(boxes)} People detected')
            cv2.imshow('frame',frame)
            count += 1
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()

        cv2.destroyAllWindows()
        cv2.waitKey(1)

    audio_thread = threading.Thread(target=record_audio)
    video_thread = threading.Thread(target=record_video)

    audio_thread.start()
    video_thread.start()
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(description='tracking')
#     parser.add_argument('--room', metavar='id', required=True,
#                         help='the room id')
#     parser.add_argument('--building', metavar='id', required=True,
#                         help='the building code')
#     args = parser.parse_args()
#     main(room=args.room, building=args.building)
