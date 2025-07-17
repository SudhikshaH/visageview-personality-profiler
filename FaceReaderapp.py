import streamlit as st
from deepface import DeepFace
from datetime import date
from PIL import Image
import os
import tempfile
from PersonalityTrait import (
    load_traits, get_generation, get_age_group, 
    get_zodiac_sign, get_summary_points,
    create_personality_card
)
import random

trait_file="traits.txt"
traits=load_traits(trait_file)

st.set_page_config(page_title="Face based Personality Predictor", layout="centered")
st.title("✨ Personality from Your Face ✨")
st.markdown("Upload your photo and birth date to get a fun, personalized personality card!")
input_file=st.file_uploader("📸 Upload a clear photo of your face", type=["jpg", "jpeg", "png"])
dob=st.date_input("📅 Select your Date of Birth",min_value=date(1945,1,1), max_value=date.today())

if input_file and dob:
    tempFile=tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
    tempFile.write(input_file.read())
    temp_file_path=tempFile.name
    with st.spinner("Analyzing face..."):
        face_data=DeepFace.analyze(temp_file_path,actions=["emotion","gender"],enforce_detection=False)[0]
    age=date.today().year - dob.year
    emotion =face_data['dominant_emotion']
    year=dob.year
    day=dob.day
    month=dob.month
    generation=get_generation(year)
    zodiac=get_zodiac_sign(day,month)
    age_group=get_age_group(age)
    summary=get_summary_points(traits,generation,zodiac, age_group, emotion)
    traits_dict={
        "💫 Expression Type": random.choice(traits["Emotion"].get(emotion.lower(), "Emotionally rich")),
        "🕰️ Life Stage Vibes": traits["AgeGroup"].get(age_group, "Mature and intuitive"),
        "🌌 Subtle Energy": traits["Zodiac"].get(zodiac, "Balanced and driven"),
        "👤 Character Flow": traits["Generation"].get(generation, "Thoughtful and bold")
    }
    output_path=os.path.join(tempfile.gettempdir(),"PersonalityCard.png")
    create_personality_card(traits_dict, summary, generation, temp_file_path, output_path)
    
    st.subheader("Your Personality Card")
    st.image(output_path, use_column_width=True)
    
    with open(output_path, "rb") as file:
        st.download_button("Download", file.read(), file_name="personalityCard.png",mime="image/png")