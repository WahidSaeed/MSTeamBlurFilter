This README is designed for the **WahidSaeed/MSTeamBlurFilter** repository. Since this project uses Python, OpenCV, and MediaPipe to replicate the background blurring effect seen in video conferencing apps, this template focuses on the technical setup and implementation.

---

# MS Teams Background Blur Filter

Ever wondered how Microsoft Teams or Zoom hides your messy room during a video call? This project explores the mechanics behind background blurring filters using **Python**, **OpenCV**, and **MediaPipe**.

## 🚀 Overview

This application uses machine learning to perform real-time **Selfie Segmentation**. By identifying the person in the video frame, we can separate the foreground from the background and apply a Gaussian blur only to the environment, keeping the user in sharp focus.

## 🛠️ Built With

* **Python**: The core programming language.
* **OpenCV**: Used for real-time computer vision processing and image manipulation.
* **MediaPipe**: Specifically the "Selfie Segmentation" solution for high-fidelity background separation.

## ✨ Features

* **Real-time Processing**: Fast enough to run on a standard webcam feed.
* **Dynamic Backgrounds**: Demonstrates how to either blur the current background or replace it with a static image (e.g., `office.jpg`).
* **Precise Masking**: Uses ML-based segmentation rather than simple color-keying.

## 💻 Getting Started

### Prerequisites

Ensure you have Python 3.x installed. You will need to install the following dependencies:

```bash
pip install opencv-python mediapipe

```

### Installation

1. **Clone the repository**:
```bash
git clone https://github.com/WahidSaeed/MSTeamBlurFilter.git
cd MSTeamBlurFilter

```


2. **Run the script**:
```bash
python main.py

```



## 📂 Project Structure

* `main.py`: The main script containing the webcam loop and MediaPipe segmentation logic.
* `office.jpg`: A sample background image for replacement testing.
* `README.md`: Project documentation.

## ⚙️ How it Works

1. **Capture**: The webcam feed is captured frame-by-frame using OpenCV.
2. **Segment**: MediaPipe processes the frame to create a binary mask (identifying "person" vs. "background").
3. **Blur**: A Gaussian blur filter is applied to the original frame.
4. **Combine**: The mask is used to stitch the sharp user (foreground) back onto the blurred background.

## 📜 License

This project is open-source and available under the MIT License.

---

**Maintained by [Wahid Saeed**](https://github.com/WahidSaeed)
