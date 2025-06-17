import streamlit as st
import numpy as np
import cv2
from PIL import Image
from symmetry import calculate_symmetry_score, generate_profiles
from golden_ratio import analyze_face_ratios
from score import compute_overall_score
from watermark import add_header  # , add_footer

# Page configuration
st.set_page_config(page_title="AI Beauty Analyzer", layout="centered")
add_header()  # 🔼 Top banner watermark

st.title("✨ AI Beauty Analyzer")

# Instructions
st.markdown("### 🧭 How to Take a Proper Selfie")
sample_image_path = "demo_images/20221109.jpg"
st.image(sample_image_path, caption="✅ Keep your face centered, well-lit, and neutral expression", use_container_width=True)


# Upload or Capture
upload_option = st.radio("Choose how to provide your selfie:", ["Upload from Device", "Take with Camera"])

if upload_option == "Upload from Device":
    uploaded_file = st.file_uploader("Upload your selfie", type=["jpg", "jpeg", "png"])
else:
    uploaded_file = st.camera_input("Take a photo using your webcam")

# Main logic after receiving image
if uploaded_file:
    img = Image.open(uploaded_file).convert('RGB')
    img_np = np.array(img)

    st.image(img, caption="Your Uploaded Selfie", use_container_width=True)

    with st.spinner("Analyzing..."):
        symmetry_score, center_line = calculate_symmetry_score(img_np)
        ratios, ratio_values = analyze_face_ratios(img_np)
        beauty_score, feedback = compute_overall_score(symmetry_score, ratios)
        left_img, right_img = generate_profiles(img_np, center_line)

    # Output Section
    st.subheader("🧠 Your Beauty Report")
    st.markdown(f"✅ **Symmetry Score:** {symmetry_score:.2f} / 100")
    st.markdown(f"✅ **Golden Ratio Match:** {ratios:.2f} / 100")
    st.markdown(f"🧠 **Overall Beauty Score:** {beauty_score:.2f} / 100")

    st.subheader("📏 Facial Measurements")
    for label, val in ratio_values.items():
        st.markdown(f"- **{label}:** {val:.1f} px")

    st.subheader("📊 Tips & Feedback")
    st.write(feedback)

    st.subheader("🖼️ Symmetrical Profile Visuals")
    col1, col2 = st.columns(2)
    col1.image(left_img, caption="Left Profile Mirror")
    col2.image(right_img, caption="Right Profile Mirror")

    # Footer (optional)
    # add_footer()
else:
    st.warning("📸 Please upload a clear, front-facing selfie to begin the analysis.")
