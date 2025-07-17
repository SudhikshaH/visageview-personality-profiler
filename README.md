Project Title - VisageView: A Streamlit App for Visual Personality Profiling Using Facial Emotion and Birth Data

**Visageview** is a fun AI powered application that combines facial expression(emotion) and date of birth to generate personality snapshot. The result is beautifully presented as a "postcard-style" image.

## Process Flow
- Upload a face image
- Uses DeepFace to analyze emotion form the face.
- Inputs your complete date of birth and then parses it to infer age group, generation and zodiac sign.
- Pulls descriptive from traits.txt file combining all the four inputs(emotion, age group, generation, zodiac sign).
- Generates a postcard size image (Image appears in the top-right corner like a stamp and personality appears as card content).
- Offers a download button to save your personality card.

## Advantages
- Provides personalized, visually appealing output based on real facial traits.
- Combines **emotion analysis** with **birth data** for deeper insights.
- Works completely offline.
- Flexible architecture as traits can be expanded or modified easily via `traits.txt`.
- Simple and interactive UI using Streamlit.
- Output is downloadable as a PNG card.

## Limitations
- This system uses DeepFace’s pre-trained models, which may fail on low-light or blurry images and Side-facing or partially visible faces.
- Traits are static — chosen randomly from a pre-written list ('traits.txt').
- No personalization using machine learning/NLP yet.
- No support for manual override (e.g., emotion correction).
- Requires TensorFlow + OpenCV which may slow down on low-resource systems.
  
## Future Improvements
- Replace static traits.txt with a semantic trait-matching model.
- Improve facial attribute prediction using fine-tuned local models.
- Enable user overrides for incorrect predictions (e.g., “I’m not sad!”)
- Add multiple trait themes (career-focused, friendship etc.)

## Tech Stack
- Streamlit - [![Streamlit](https://img.shields.io/badge/Streamlit-Framework-red?logo=streamlit)](https://streamlit.io/)
- DeepFace - [![DeepFace](https://img.shields.io/badge/DeepFace-GitHub-blue?logo=github)](https://github.com/serengil/deepface)
- Pillow - [![Pillow](https://img.shields.io/badge/Pillow-Image%20Processing-blueviolet)](https://pillow.readthedocs.io/en/stable/)
- OpenCV - [![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-critical?logo=opencv)](https://opencv.org/)
- TextWrap - [![Textwrap](https://img.shields.io/badge/Textwrap-Built--in-lightgrey)](https://docs.python.org/3/library/textwrap.html)

## Installation

Install all required dependencies:

```bash
pip install streamlit deepface pillow opencv-python

## Author
SUDHIKSHA H

[🔗 LinkedIn](https://www.linkedin.com/in/sudhiksha-h)
