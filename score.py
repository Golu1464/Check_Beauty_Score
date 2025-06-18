# score.py
def compute_overall_score(symmetry, golden_ratio, extra_metrics=None):
    # Give symmetry 40%, golden ratio 40%, and extra features 20%
    base = 0.4 * symmetry + 0.4 * golden_ratio

    eye_score = 0
    if extra_metrics:
        eye_distance = extra_metrics.get("Eye Distance", 0)
        face_width = extra_metrics.get("Face Width", 1)
        eye_spacing_ratio = eye_distance / face_width

        if 0.28 < eye_spacing_ratio < 0.36:
            eye_score = 100
        elif eye_spacing_ratio <= 0.26 or eye_spacing_ratio >= 0.38:
            eye_score = 60
        else:
            eye_score = 80

        base += 0.2 * eye_score
    else:
        base += 0.2 * 75  # default middle score

    # Clamp final score from 20 to 100
    final_score = min(100, max(20, base))

    # Feedback logic stays the same
    tips = []
    if symmetry > 90:
        tips.append("✅ Exceptional facial symmetry — a trait often admired.")
    elif symmetry > 75:
        tips.append("🔹 Mild asymmetry — completely natural and common.")
    else:
        tips.append("🔹 Faces aren’t meant to be perfect — asymmetry adds character!")

    if golden_ratio > 90:
        tips.append("✅ Your face aligns beautifully with the golden ratio.")
    elif golden_ratio > 75:
        tips.append("🔹 Slight deviation from golden ratio — uniqueness is beauty.")
    else:
        tips.append("🔹 Beauty isn’t defined by math — even celebrities defy ratios!")

    if extra_metrics:
        if 0.28 < eye_spacing_ratio < 0.36:
            tips.append("✅ Balanced eye spacing gives your face natural harmony.")
        elif eye_spacing_ratio <= 0.26:
            tips.append("🔹 Slightly close-set eyes — gives intensity and focus.")
        else:
            tips.append("🔹 Slightly wide-set eyes — often seen as calming and open.")

    tips.append("🌟 Remember: Beauty is personal, diverse, and not defined by numbers.")

    return round(final_score, 2), "\n".join(tips)
