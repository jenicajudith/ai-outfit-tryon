# Virtual Try-On Glasses using OpenCV

This project allows users to virtually try on glasses in real-time using their webcam. It uses OpenCV and MediaPipe to detect facial landmarks and overlay a transparent glasses image on the eyes.

---

## ✅ Features

- Real-time face landmark detection  
- Transparent glasses overlay  
- Works with webcam input  
- Easy to customize with different glasses  

---

## 📦 Requirements

- Python 3.7 or above  
- OpenCV  
- MediaPipe  
- NumPy  

Install all dependencies using:

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install opencv-python mediapipe numpy
```

---

## 🚀 How to Run

1. Clone or download the project.
2. Ensure your webcam is connected.
3. Run the script:

```bash
python virtual_try_on_glasses.py
```

4. The webcam feed will open, showing the glasses overlaid on your face.
5. Press **`q`** to quit the program.

---

## 🧠 How It Works

- The script uses **MediaPipe** to detect key facial landmarks (such as the eyes).
- It overlays a transparent glasses image onto the eyes based on these landmarks.
- You can easily customize the glasses image to fit your desired style or design.

---

## 📁 File Structure

```
virtual-try-on-glasses/
├── virtual_try_on_glasses.py
├── requirements.txt
└── README.md
```

---

## 🔮 Future Improvements

- Support for multiple glasses styles
- Improved glasses fitting using more precise facial landmarks
- Ability to adjust glasses size based on face dimensions

---

## 📜 License

This project is open-source and free to use for educational purposes.
