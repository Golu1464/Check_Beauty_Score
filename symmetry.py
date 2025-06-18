# symmetry.py
import cv2
import mediapipe as mp
import numpy as np

mp_face = mp.solutions.face_mesh

def calculate_symmetry_score(image):
    face = mp_face.FaceMesh(static_image_mode=True)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face.process(rgb)

    if not results.multi_face_landmarks:
        raise ValueError("No face detected. Please upload a clearer front-facing photo.")

    landmarks = results.multi_face_landmarks[0].landmark
    width = image.shape[1]

    symmetric_pairs = [
        (234, 454), (93, 323), (132, 361), (58, 288), (127, 356),
        (50, 280), (101, 330), (205, 425), (98, 327), (55, 285),
        (65, 295), (107, 336), (52, 282), (66, 296), (3, 13)
    ]

    diffs = [abs(landmarks[i].x - (1 - landmarks[j].x)) for i, j in symmetric_pairs]
    mean_diff = np.mean(diffs)
    score = max(0, 100 - mean_diff * 1000)

    return round(score, 2), width // 2, results.multi_face_landmarks[0]

def generate_profiles(image, center_line):
    left_half = image[:, :center_line]
    right_half = image[:, center_line:]
    left_mirror = cv2.flip(left_half, 1)
    right_mirror = cv2.flip(right_half, 1)
    left_symmetry = np.concatenate((left_half, left_mirror), axis=1)
    right_symmetry = np.concatenate((right_mirror, right_half), axis=1)
    return left_half, right_half, left_symmetry, right_symmetry
