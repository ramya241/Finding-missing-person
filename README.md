# Finding Missing Person Using AI

An AI-powered missing person detection system built using Facial Recognition, Image Processing, and Machine Learning techniques.

This project helps identify missing persons by comparing uploaded images with stored facial encodings using computer vision algorithms.

---

# Features

- Face Detection using OpenCV & Dlib
- Facial Recognition with AI models
- Missing person database management
- Upload and compare images
- Real-time face matching
- User-friendly interface
- Secure authentication system

---

# Tech Stack

## Frontend
- Streamlit / HTML / CSS

## Backend
- Python

## AI & Computer Vision
- OpenCV
- Dlib
- Face Recognition Library
- NumPy

## Database
- PostgreSQL / SQLite

---

# Project Structure

```bash
Finding-missing-person/
│
├── face_encoding/
├── models/
├── pages/
├── resources/
├── Home.py
├── mobile_app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/ramya241/Finding-missing-person.git
```

## Navigate to Project Folder

```bash
cd Finding-missing-person
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run the Application

```bash
streamlit run Home.py
```

---

# How It Works

1. User uploads an image of a missing person
2. System extracts facial features
3. Facial encodings are generated
4. Uploaded image is compared with stored database
5. Matching results are displayed with confidence score

---

# Future Improvements

- Live CCTV integration
- Mobile application support
- Cloud deployment
- SMS/Email alerts
- Multi-face tracking
- Deep learning enhancement

---

# Security Note

Sensitive files such as:

```bash
key.json
.env
credentials/
```

should never be uploaded to GitHub.

Add them to `.gitignore`.

---

# Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch
3. Commit changes
4. Push to your branch
5. Open a Pull Request

---

# License

This project is developed for educational and research purposes.

---

# Author

Ramya

GitHub:
https://github.com/ramya241