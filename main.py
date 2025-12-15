import time
import cv2

from camera import Camera
from emotion_engine import EmotionEngine
from tracker import EmotionTracker
from logger import EmotionLogger
from dashboard import Dashboard


ANALYZE_EVERY = 0.6  # seconds


def main():
    camera = Camera()
    engine = EmotionEngine()
    tracker = EmotionTracker(window_size=12)
    logger = EmotionLogger()
    dashboard = Dashboard()

    last_time = 0

    while True:
        frame = camera.read()
        if frame is None:
            break

        if time.time() - last_time > ANALYZE_EVERY:
            scores = engine.analyze(frame)
            tracker.update(scores)

            smooth_scores = tracker.smoothed()
            dominant, confidence = tracker.dominant_emotion()

            logger.log(smooth_scores, dominant)
            last_time = time.time()
        else:
            smooth_scores = tracker.smoothed()
            dominant, confidence = tracker.dominant_emotion()

        dashboard.draw(frame, smooth_scores, dominant, confidence)
        cv2.imshow("Emotion Analytics System", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
