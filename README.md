# Persian Slide Progress Bar Generator 🎯

This repository contains Python scripts for generating **slide progress bar images** with **Persian chapter titles** for presentations. The scripts generate a visually appealing progress bar for each slide, with dynamic bullet indicators representing the progress through chapters and slides.

---

## ✨ Features

- **Customizable** chapter titles in Persian.
- **Progress bullets** for each slide to track presentation progress.
- **Highlight the current slide** with a distinct color.
- **Color themes** and clean design for better presentation visuals.
- **Supports Persian text rendering** using `arabic_reshaper` and `python-bidi` libraries for proper right-to-left alignment.

---

## 📁 Scripts Included

### `bulletprogressbar.py`
- **Basic version**: Generates simple progress bars for each chapter.
- Does not highlight the active chapter.

### `bulletprogressbar-customcolor.py`
- Custom **color scheme** for the progress bar.
- Enhanced **layout** with space between chapters for clarity.

### `bulletprogressbar-customcolorv2.py`
- **Active chapter highlight** with better visual feedback.
- **Sophisticated color coding** (current slide in pink).
- Adjusted **text position** for better alignment and clearer visualization.

---

## 🧪 Requirements

To run the scripts, you'll need to install the following Python libraries:

```bash
pip install pillow arabic-reshaper python-bidi
