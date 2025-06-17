import cv2
import mediapipe as mp
import numpy as np

mp_face = mp.solutions.face_mesh

def calculate_symmetry_score(image):
    face = mp_face.FaceMesh(static_image_mode=True)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face.process(rgb)
    if not results.multi_face_landmarks:
        return 0, image.shape[1] // 2

    landmarks = results.multi_face_landmarks[0].landmark
    width = image.shape[1]

    left_pts = [landmarks[i].x for i in range(0, 468) if landmarks[i].x < 0.5]
    right_pts = [1 - landmarks[i].x for i in range(0, 468) if landmarks[i].x > 0.5]

    # Safely compute difference using zip (avoids broadcasting error)
    diff = [abs(l - r) for l, r in zip(left_pts, right_pts)]
    score = max(0, 100 - np.mean(diff) * 1000)

    return score, width // 2

def generate_profiles(image, center_line):
    left_profile = image[:, :center_line]
    right_profile = image[:, center_line:]

    # Flip the right profile to create a mirror effect
    right_profile = cv2.flip(right_profile, 1)

    return left_profile, right_profile