# 🖼️ Image Background Remover & Format Converter

## 🚀 Overview

This is a simple yet powerful web-based tool that allows users to:

- Remove the background from images using AI.
- Convert images into different formats (WEBP, JPEG, PNG, JPG).
- Download the processed images with customizable filenames.

Built with **Streamlit** and **Rembg**, this app provides an intuitive interface for seamless image processing. 🎨

🚀 **Live Demo:**  
[![Try It](https://img.shields.io/badge/BG%20%26%20Format%20Here-blue?style=for-the-badge)](https://bgandformat.streamlit.app/)


## ✨ Features

- 📤 **Upload images** in WEBP, JPEG, PNG, or JPG format.
- 🧑‍🎨 **Remove image backgrounds** with AI.
- 🎭 **Convert image formats** to WEBP, JPEG, PNG, or JPG.
- 📝 **Customize filenames** before downloading.
- ⏬ **Download high-quality processed images**.

## 🛠️ Installation Guide

To run this project locally, follow these steps:

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Rktim/Image_BG_format.git
cd Image_BG_format
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the App

```bash
streamlit run app.py
```

## 🏗️ How It Works

1. **Upload** your image.
2. **Choose an operation** (Remove Background or Convert Format).
3. **Customize the filename** if needed.
4. **Download** the processed image.

## 📦 Dependencies

- `streamlit`
- `rembg`
- `Pillow`
- `io`

## 🤖 Troubleshooting

If you encounter an error related to `onnxruntime`, try installing it manually:

```bash
pip install onnxruntime
```

This may be required by the `rembg` library for AI-based background removal.

## 🌟 Contributing

Feel free to fork this repo and contribute improvements! If you encounter any issues, open an issue or submit a pull request.

## 📜 License

This project is licensed under the[LICENSE](LICENSE). You are free to modify and distribute it as per the terms of the license.

---

💡 Created with ❤️ by Raktim 
