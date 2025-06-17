# ✨ AI Beauty Analyzer

The **AI Beauty Analyzer** is a Streamlit-based web application that uses facial landmark detection to analyze the symmetry and golden ratio of a user's face from a selfie. It then generates a beauty score, facial measurements, personalized feedback, and visualized mirrored profiles.

## 🚀 Features

- 📷 Upload or capture a selfie
- 🧠 Analyze facial symmetry and golden ratio
- 📏 Display key facial measurements (face width, length, eye distance, etc.)
- 🪞 Generate mirrored profile views
- ✅ Get a beauty score and improvement tips

## 🧰 Tech Stack

- Python
- OpenCV
- MediaPipe
- Streamlit
- NumPy
- Pillow (PIL)

## 📸 How to Take a Good Selfie

- Center your face in the frame
- Ensure even lighting
- Use a neutral expression
- Avoid heavy filters

## 🛠️ Setup Instructions

1. **Clone the repository**  
```bash
git clone https://github.com/Golu1464/Beauty_Analyzer_APP.git
cd ai-beauty-analyzer


Create a virtual environment & activate it

python -m venv myenv
# Windows
myenv\Scripts\activate
# macOS/Linux
source myenv/bin/activate


Install dependencies

pip install -r requirements.txt

Run the app

streamlit run app.py
