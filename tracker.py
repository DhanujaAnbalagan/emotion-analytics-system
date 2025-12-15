from collections import deque

EMOTIONS = ["angry", "happy", "sad", "surprise", "neutral"]


class EmotionTracker:
    def __init__(self, window_size=10):
        self.window_size = window_size
        self.history = {e: deque(maxlen=window_size) for e in EMOTIONS}

    def update(self, scores):
        for e in EMOTIONS:
            self.history[e].append(scores.get(e, 0.0))

    def smoothed(self):
        smooth = {}
        for e in EMOTIONS:
            if self.history[e]:
                smooth[e] = sum(self.history[e]) / len(self.history[e])
            else:
                smooth[e] = 0.0
        return smooth

    def dominant_emotion(self):
        smooth = self.smoothed()
        emotion = max(smooth, key=lambda e: smooth[e])
        confidence = int(smooth[emotion])
        return emotion, confidence
