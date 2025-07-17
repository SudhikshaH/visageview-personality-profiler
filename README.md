Project Title - VisageView: A Streamlit App for Visual Personality Profiling Using Facial Emotion and Birth Data

**Visageview** is a fun AI powered application that combines facial expression(emotion) and date of birth to generate personality snapshot. This is presented as a postcard.

**Process Flow**
- Upload a face image
- Use DeepFace to analyze emotion form the face.
- Takes your complete date of birth and then parses to infer age group, generation and zodiac sign.
- Pulls details traits.txt file combining all the four traits (emotion, age group, generation, zodiac sign).
- Generates a postcard size image (Image uploaded appear at the top right corner of stamp size and personality as content to the postcard).
- Download option is available to download the snapshot of your personality.

**Advantage**
- Provides personalized, visually appealing output based on real facial traits.
- Combines **emotion analysis** with **birth data** for deeper insights.
- Works completely offline.
- Flexible architecture as traits can be expanded or modified easily via `traits.txt`.
- Simple and interactive UI using Streamlit.
- Output is downloadable as a high-quality PNG card.

**Disadvnatage**
- This system uses DeepFace’s pre-trained models, which may fail on Low-light or blurry images and Side-facing or partially visible faces.
- The traits.txt system is rule-based and static and doesn’t use NLP or embeddings to match personality style.
- No deep learning personalization as sentences are pre-written.
- Override emotion with mood is not considered.
- DeepFace requires TensorFlow and OpenCV, which can slow down on systems without GPU.

**Future Improvements**
- Replace static traits.txt with a semantic trait-matching model.
- Improve facial attribute prediction using fine-tuned local models.
- Enable user overrides for incorrect predictions (e.g., “I’m not sad!”)
- Add multiple trait themes (career-focused, friendship etc.)

**Tech Stack**
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Framework-red?logo=streamlit)](https://streamlit.io/)
[![DeepFace](https://img.shields.io/badge/DeepFace-GitHub-blue?logo=github)](https://github.com/serengil/deepface)
[![Pillow](https://img.shields.io/badge/Pillow-Image%20Processing-blueviolet)](https://pillow.readthedocs.io/en/stable/)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-critical?logo=opencv)](https://opencv.org/)
[![Textwrap](https://img.shields.io/badge/Textwrap-Built--in-lightgrey)](https://docs.python.org/3/library/textwrap.html)

**Installation Dependencies**
pip install streamlit deepface pillow opencv-python

