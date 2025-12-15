import csv
from datetime import datetime


class EmotionLogger:
    def __init__(self, filename="emotion_log.csv"):
        self.filename = filename
        self._init_file()

    def _init_file(self):
        with open(self.filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "timestamp",
                "angry",
                "happy",
                "sad",
                "surprise",
                "neutral",
                "dominant_emotion"
            ])

    def log(self, scores, dominant):
        with open(self.filename, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                scores["angry"],
                scores["happy"],
                scores["sad"],
                scores["surprise"],
                scores["neutral"],
                dominant
            ])
