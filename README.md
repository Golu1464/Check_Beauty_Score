# ✨ AI Beauty Analyzer

The **AI Beauty Analyzer** is a Streamlit-powered web application that uses AI to assess facial beauty. It calculates facial symmetry and golden ratio from selfies and provides feedback, measurements, and mirrored profile visuals.

## 🚀 Features

- 📸 Upload or capture a selfie using webcam  
- 🧠 AI-based facial analysis (symmetry + golden ratio)  
- 📏 Display of facial proportions and measurements  
- 💡 Beauty score with improvement tips  
- 🪞 Left and right mirrored facial profile generation  

## 🛠️ Built With

- Python
- Streamlit
- OpenCV
- MediaPipe
- NumPy
- Pillow

## 📸 Selfie Guidelines

To get the best results:
- Use good lighting (avoid shadows)
- Keep your face straight and neutral
- Avoid glasses or filters
- Ensure the entire face is visible

## ⚙️ Installation & Running

```bash
# Clone the repository
git clone https://github.com/Golu1464/Check_Beauty_Score.git
cd Check_Beauty_Score

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
