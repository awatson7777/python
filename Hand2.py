import cv2
import mediapipe as mp

mphands = mp.solutions.hands
hands = mphands.Hands()
mpdrawing = mp.solutions.drawing_utils
cap = cv2.VideoCapture("woodclip1.mp4")

_, frame = cap.read()

h, w, c = frame.shape

while True:
    _, frame = cap.read()
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(framergb)
    hand_landmarks = results.multi_hand_landmarks
    if hand_landmarks:
        for handLMs in hand_landmarks:
            x_max = 0
            y_max = 0
            x_min = w
            y_min = h
            for lm in handLMs.landmark:
                x, y = int(lm.x * w), int(lm.y * h)
                if x > x_max:
                    x_max = x
                if x < x_min:
                    x_min = x
                if y > y_max:
                    y_max = y
                if y < y_min:
                    y_min = y
                    mpdrawing.draw_landmarks(frame, handLMs, mphands.HAND_CONNECTIONS)
                    cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

                    cv2.imshow("Frame", frame)
                    cv2.waitKey(1)

                    while cap.isOpened():
                        ret, frame = cap.read()
                        cv2.imshow("video", frame)
                        key = cv2.waitKey(0)
                        while key not in [ord('q'), ord('k')]:
                            key = cv2.waitKey(0)
                        if key == ord('q'):
                            break

                if results.multi_hand_landmarks != None:
                    for hand_landmarks in results.multi_hand_landmarks:
                        for point in mphands.HandLandmark:

                            normalizedLandmark = hand_landmarks.landmark[point]
                            pixelCoordinatesLandmark = mpdrawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                          normalizedLandmark.y,
                                                                                          w, h)

                            print(point)
                            print(pixelCoordinatesLandmark)
                            print(normalizedLandmark)