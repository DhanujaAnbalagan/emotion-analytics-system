import cv2

WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
GRAY = (80, 80, 80)


class Dashboard:
    def draw(self, frame, scores, dominant, confidence):
        h, w, _ = frame.shape

        cv2.rectangle(frame, (0, 0), (w, 45), (0, 0, 0), -1)
        cv2.putText(frame, "REAL-TIME EMOTION ANALYTICS",
                    (15, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, CYAN, 2)

        label = f"{dominant.upper()} ({confidence}%)"
        cv2.putText(frame, label,
                    (w // 2 - 120, h - 25),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, WHITE, 2)

        bar_x = 20
        bar_y = 70
        bar_w = 180
        bar_h = 18

        for i, (emo, val) in enumerate(scores.items()):
            y = bar_y + i * 30

            cv2.putText(frame, emo,
                        (bar_x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, WHITE, 1)

            cv2.rectangle(frame,
                          (bar_x + 80, y - bar_h),
                          (bar_x + 80 + bar_w, y),
                          GRAY, -1)

            fill = int((val / 100) * bar_w)
            cv2.rectangle(frame,
                          (bar_x + 80, y - bar_h),
                          (bar_x + 80 + fill, y),
                          CYAN if emo == dominant else WHITE,
                          -1)

        cv2.putText(frame, "Press Q to exit",
                    (w - 180, h - 15),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, WHITE, 1)
