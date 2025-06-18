# app.py
import streamlit as st
import numpy as np
import cv2
from PIL import Image
from symmetry import calculate_symmetry_score, generate_profiles
from golden_ratio import analyze_face_ratios, is_face_centered_and_clear
from score import compute_overall_score
from watermark import add_header  # Optional footer can be added

# Page configuration
st.set_page_config(page_title="AI Beauty Analyzer", layout="centered")

# Add custom header
add_header()

st.title("\u2728 Your Personalized Face Harmony Report")
st.markdown("""
Your face is unique — this app gives you kind insights based on science, not judgment. 
Embrace your features and explore how facial balance works! 💖
""")

# Sample instructions
st.markdown("### 🧽 How to Take a Proper Selfie")
sample_image_path = "demo_images/20221109.jpg"
st.image(sample_image_path, caption="✅ Keep your face centered, well-lit, and with a neutral expression", use_container_width=True)

upload_option = st.radio("Choose how to provide your selfie:", ["Upload from Device", "Take with Camera"])

if upload_option == "Upload from Device":
    uploaded_file = st.file_uploader("Upload your selfie", type=["jpg", "jpeg", "png"])
else:
    uploaded_file = st.camera_input("Take a photo using your webcam")

if uploaded_file:
    img = Image.open(uploaded_file).convert('RGB')
    img_np = np.array(img)

    st.image(img, caption="Your Uploaded Selfie", use_container_width=True)

    with st.spinner("Analyzing..."):
        try:
            symmetry_score, center_line, landmarks = calculate_symmetry_score(img_np)

            if not is_face_centered_and_clear(img_np, landmarks):
                st.warning("⚠️ Face may not be centered or bright enough. This may reduce accuracy.")

            golden_score, measurements = analyze_face_ratios(img_np, landmarks)

            overall_score, feedback = compute_overall_score(symmetry_score, golden_score, measurements)
            # === Improved Overall Beauty Score ===
            # Weighted average with sharper spread
            weighted_sum = (0.35 * symmetry_score + 0.25 * golden_score + 0.4 * overall_score)
            beauty_score_raw = weighted_sum / 100  # Normalize to 0–1

            # Apply non-linear scale — more aggressive curve
            scaled_score = beauty_score_raw ** 1.8  # Sharper slope for better spread
            overall_beauty_score = round(4 + scaled_score * 9, 1)  # Map to 1–10
            overall_beauty_score = min(10.0, max(1.0, overall_beauty_score))  # Clamp


            # === Improved Uniqueness Score — Without Randomness ===
            asymmetry_factor = abs(50 - symmetry_score) / 50
            golden_ratio_deviation = abs(60 - golden_score) / 60
            harmony_variation = abs(70 - overall_score) / 70

            uniqueness_raw = 0.4 * asymmetry_factor + 0.3 * golden_ratio_deviation + 0.3 * harmony_variation

            uniqueness_score = 5 + 4 * uniqueness_raw  # removed randomness
            uniqueness_score = round(min(10.0, max(1.0, uniqueness_score)), 1)



            left_img, right_img, mirrored_left, mirrored_right = generate_profiles(img_np, center_line)
        except Exception as e:
            st.error(f"Error: {e}")
            st.stop()

    st.subheader("🧠 Your Face Harmony Report")
    st.markdown(f"✅ **Symmetry Score:** {symmetry_score:.2f} / 100")
    st.markdown(f"✅ **Golden Ratio Match:** {golden_score:.2f} / 100")
    st.markdown(f"🧠 **Facial Harmony Score:** {overall_score:.2f} / 100")
    st.markdown(f"💖 **Overall Beauty Score:** {overall_beauty_score} / 10")
    st.markdown(f"🌟 **Uniqueness Score:** {uniqueness_score} / 10")


    st.subheader("📏 Facial Measurements")

    for label, value in measurements.items():
        if isinstance(value, (int, float)):
            st.markdown(f"- **{label}:** {value:.1f} px")
        elif isinstance(value, dict):
            st.markdown(f"- **{label}:**")
            for sub_label, sub_value in value.items():
                st.markdown(f"  - {sub_label}: {sub_value}")
        else:
            st.markdown(f"- **{label}:** {value}")

    st.subheader("📊 Personalized Feedback")
    st.write(feedback)

    with st.expander("💡 Why this score doesn't define your beauty"):
        st.write("""
        - A face can't be measured like a math problem.
        - Many iconic people have unusual features that make them unforgettable.
        - This is just a fun experiment with science — you are already amazing.
        """)

    st.subheader("🖼️ Symmetrical Profile Visuals")
    col1, col2, col3, col4 = st.columns(4)
    col1.image(left_img, caption="Left Profile", use_container_width=True)
    col2.image(right_img, caption="Right Profile", use_container_width=True)
    col3.image(mirrored_left, caption="Full Face (from Left)", use_container_width=True)
    col4.image(mirrored_right, caption="Full Face (from Right)", use_container_width=True)
else:
    st.warning("📸 Please upload or capture a clear, front-facing selfie to begin the analysis.")
