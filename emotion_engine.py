from deepface import DeepFace

EMOTIONS = ["angry", "happy", "sad", "surprise", "neutral"]


class EmotionEngine:
    def analyze(self, frame):
        try:
            result = DeepFace.analyze(
                frame,
                actions=["emotion"],
                enforce_detection=False
            )
            raw = result[0]["emotion"]

            scores = {e: float(raw.get(e, 0.0)) for e in EMOTIONS}
            return scores

        except Exception:
            return {e: 0.0 for e in EMOTIONS}
