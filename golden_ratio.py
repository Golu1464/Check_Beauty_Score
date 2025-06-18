# golden_ratio.py
import numpy as np
import cv2
import mediapipe as mp

mp_face = mp.solutions.face_mesh

def analyze_face_ratios(image, landmarks_obj):
    h, w = image.shape[:2]
    landmarks = landmarks_obj.landmark

    def point(idx):
        return int(landmarks[idx].x * w), int(landmarks[idx].y * h)

    def dist(p1, p2):
        return np.linalg.norm(np.array(p1) - np.array(p2))

    # Key landmarks
    top = point(10)
    bottom = point(152)
    left = point(234)
    right = point(454)
    eye_left = point(133)
    eye_right = point(362)
    mouth_left = point(61)
    mouth_right = point(291)
    nose_tip = point(1)
    chin = point(152)
    upper_lip = point(13)
    lower_lip = point(14)

    # Measurements
    face_length = dist(top, bottom)
    face_width = dist(left, right)
    eye_distance = dist(eye_left, eye_right)
    mouth_width = dist(mouth_left, mouth_right)
    nose_to_chin = dist(nose_tip, chin)
    lip_height = dist(upper_lip, lower_lip)

    # Ratios to compare
    ratios_used = {
        "Face Length / Face Width": face_length / face_width if face_width else 0,
        "Eye Distance / Mouth Width": eye_distance / mouth_width if mouth_width else 0,
        "Eye Distance / Face Width": eye_distance / face_width if face_width else 0,
        "Nose to Chin / Face Length": nose_to_chin / face_length if face_length else 0,
        "Lip Height / Mouth Width": lip_height / mouth_width if mouth_width else 0
    }

    # Golden targets
    ideal_ratios = {
        "Face Length / Face Width": 1.618,
        "Eye Distance / Mouth Width": 1.618,
        "Eye Distance / Face Width": 0.32,
        "Nose to Chin / Face Length": 0.618,
        "Lip Height / Mouth Width": 0.2
    }

    # Calculate deviation score
    deviations = []
    for key in ratios_used:
        actual = ratios_used[key]
        ideal = ideal_ratios[key]
        rel_error = abs(actual - ideal) / ideal
        deviations.append(rel_error)

    avg_deviation = np.mean(deviations)

    # Score using an exponential decay function (good distribution)
    score = 100 * np.exp(-5 * avg_deviation)
    score = round(score, 2)

    values = {
        "Face Length": round(face_length, 2),
        "Face Width": round(face_width, 2),
        "Eye Distance": round(eye_distance, 2),
        "Mouth Width": round(mouth_width, 2),
        "Nose to Chin": round(nose_to_chin, 2),
        "Lip Height": round(lip_height, 2),
        "Golden Ratio Score": score,
        "Ratios Compared": {k: round(ratios_used[k], 3) for k in ratios_used}
    }

    return score, values


def is_face_centered_and_clear(image, face_landmarks):
    h, w = image.shape[:2]
    nose_tip = face_landmarks.landmark[1]
    nose_x = nose_tip.x * w
    center_offset = abs(nose_x - (w / 2)) / w
    brightness = np.mean(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))
    return center_offset < 0.15 and brightness > 60
