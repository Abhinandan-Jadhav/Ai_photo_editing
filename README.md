# 🖼️ AI Photo Editor

A modern web-based **AI Photo Editor** built using **Python Flask, OpenCV, NumPy, HTML, CSS, and JavaScript**.

This project allows users to upload an image, apply different image-processing techniques, preview the processed result, and download the edited image.

---

## ✨ Features

### 🎨 Image Processing

The application provides the following image-processing operations:

* Grayscale Conversion
* Binary Image Conversion
* RGB to HSV Conversion
* Gaussian Blur
* Brightness Adjustment
* Contrast Adjustment
* Edge Detection
* Image Sharpening
* Dilation
* Erosion
* Opening
* Closing

### 🌐 Web Features

* Modern responsive user interface
* Drag-and-drop image upload
* Image file validation
* Original image preview
* Processed image preview
* Download processed image
* Mobile-friendly design
* Animated background interface
* Fast local image processing

---

## 🛠️ Technologies Used

| Technology | Purpose                         |
| ---------- | ------------------------------- |
| Python     | Backend programming             |
| Flask      | Web application framework       |
| OpenCV     | Image processing                |
| NumPy      | Numerical and matrix operations |
| HTML5      | Web page structure              |
| CSS3       | User interface and animations   |
| JavaScript | Frontend interaction            |
| Jinja2     | Flask HTML templating           |

---

## 📂 Project Structure

```text
AI-Photo-Editor/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    │
    ├── style.css
    ├── script.js
    │
    ├── uploads/
    │   └── .gitkeep
    │
    └── output/
        └── .gitkeep
```

---

## ⚙️ How the Project Works

The basic workflow of the application is:

```text
User
  ↓
Upload Image
  ↓
Flask Web Application
  ↓
OpenCV Image Processing
  ↓
Selected Filter
  ↓
Processed Image
  ↓
Preview Result
  ↓
Download Image
```

---

## 🔍 Image Processing Operations

### 1. Grayscale

Converts a color image into a grayscale image containing different shades of gray.

### 2. Binary

Converts the image into a black-and-white image using thresholding.

### 3. RGB to HSV

Converts the image from the BGR/RGB color representation to the HSV color space.

HSV represents:

* Hue
* Saturation
* Value

### 4. Gaussian Blur

Applies Gaussian filtering to reduce image noise and smooth the image.

### 5. Brightness

Changes the brightness level of the image using OpenCV intensity scaling.

### 6. Contrast

Adjusts the difference between dark and bright areas of the image.

### 7. Edge Detection

Uses the Canny edge detection algorithm to identify important boundaries in the image.

### 8. Sharpening

Enhances image details and makes edges appear sharper.

### 9. Dilation

Expands bright regions and can be used to strengthen objects or connected regions.

### 10. Erosion

Shrinks bright regions and can be used to remove small unwanted regions.

### 11. Opening

Performs erosion followed by dilation and is useful for removing small noise.

### 12. Closing

Performs dilation followed by erosion and is useful for filling small gaps.

---

# 💻 Installation

## Step 1: Clone the Repository

```powershell
git clone https://github.com/Abhinandan-Jadhav/Ai_photo_editing.git
```

Go into the project directory:

```powershell
cd Ai_photo_editing
```

---

## Step 2: Create a Virtual Environment

For Windows:

```powershell
python -m venv .venv
```

---

## Step 3: Activate the Virtual Environment

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate again:

```powershell
.\.venv\Scripts\Activate.ps1
```

---

## Step 4: Install Dependencies

```powershell
python -m pip install -r requirements.txt
```

---

## Step 5: Run the Application

```powershell
python app.py
```

The application will start on:

```text
http://127.0.0.1:5000
```

Open this address in your web browser.

---

# 📦 Requirements

The project uses the following Python packages:

```text
Flask
OpenCV
NumPy
Werkzeug
```

All required packages are listed in:

```text
requirements.txt
```

---

# 🖥️ Usage

1. Open the application in your browser.
2. Upload a JPG, JPEG, PNG, or WEBP image.
3. Select an image-processing filter.
4. Adjust the available parameters if required.
5. Click **Apply Filter**.
6. View the original and processed images.
7. Click **Download Processed Image** to save the result.

---

# 📸 Supported Image Formats

The application supports:

```text
JPG
JPEG
PNG
WEBP
```

Maximum upload size:

```text
16 MB
```

---

# 🔐 Security Features

The application includes basic security and validation features:

* Allowed file-extension validation
* Secure filename handling
* Unique filenames for uploaded images
* Maximum upload-size restriction
* Invalid image detection
* Separate upload and output directories

---

# 📱 Responsive Design

The interface is designed to work on:

* Desktop
* Laptop
* Tablet
* Mobile devices

The layout automatically adjusts according to the screen size.

---

# 🚀 Future Enhancements

The project can be extended with additional features such as:

* AI background removal
* Face detection
* Object detection
* Automatic image enhancement
* Image rotation
* Image cropping
* Image resizing
* Watermark addition
* Face beautification
* Background replacement
* AI image restoration
* User login system
* Image editing history
* Cloud image storage
* Before/after comparison slider

---

# 🎓 Project Objective

The main objective of this project is to develop a simple and interactive web-based image editor using computer vision techniques.

The project demonstrates how **Flask can be combined with OpenCV and NumPy** to create a practical image-processing web application.

---

# 📚 Learning Outcomes

Through this project, the following concepts can be learned:

* Python Flask web development
* HTML, CSS and JavaScript
* Image upload handling
* OpenCV image processing
* NumPy image manipulation
* Color-space conversion
* Image filtering
* Edge detection
* Morphological operations
* Web application development
* Frontend and backend integration

---

# 👨‍💻 Project Developers

**Abhinandan Jadhav**
**Rakshita kamble**
**Mahesh Nesarkar**
**Suddep H**

---

# 📄 License

This project is developed for educational and academic purposes.

You are free to modify and improve the project for learning and demonstration purposes.

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

**AI Photo Editor — Edit. Enhance. Transform.**
