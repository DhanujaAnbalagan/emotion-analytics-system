import cv2


class Camera:
    def __init__(self, cam_index=0):
        self.cap = cv2.VideoCapture(cam_index)

    def read(self):
        ret, frame = self.cap.read()
        if not ret:
            return None
        return cv2.flip(frame, 1)

    def release(self):
        self.cap.release()
