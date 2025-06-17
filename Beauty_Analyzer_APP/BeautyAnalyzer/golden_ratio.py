import cv2 
import mediapipe as mp

mp_face = mp.solutions.face_mesh

def analyze_face_ratios(image):
    face = mp_face.FaceMesh(static_image_mode=True)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face.process(rgb)

    if not results.multi_face_landmarks:
        return 0, {}

    landmarks = results.multi_face_landmarks[0].landmark
    h, w = image.shape[:2]

    def point(idx):
        return int(landmarks[idx].x * w), int(landmarks[idx].y * h)

    top, bottom = point(10), point(152)
    left, right = point(234), point(454)
    eye_left, eye_right = point(133), point(362)
    mouth_left, mouth_right = point(61), point(291)

    face_length = abs(bottom[1] - top[1])
    face_width = abs(right[0] - left[0])
    eye_distance = abs(eye_right[0] - eye_left[0])
    mouth_width = abs(mouth_right[0] - mouth_left[0])

    ratio = face_length / face_width if face_width != 0 else 0
    match_score = 100 - abs(ratio - 1.618) * 100

    values = {
        "Face Length": face_length,
        "Face Width": face_width,
        "Eye Distance": eye_distance,
        "Mouth Width": mouth_width,
        "Golden Ratio": ratio
    }

    return match_score, values
