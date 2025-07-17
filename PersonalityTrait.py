from deepface import DeepFace
from datetime import date
import random
from PIL import Image, ImageDraw, ImageFont
import textwrap

def get_generation(year):
    if year>=2013:
        return "Gen Alpha"
    elif 1997<=year<=2012:
        return "Gen Z"
    elif 1981<=year<=1996:
        return "Millennial"
    elif 1965<=year<=1980:
        return "Gen X"
    elif 1946<= year <=1964:
        return "Baby Boomer"
    return "Silent Generation"
    
def get_age_group(age):
    if age<13:
        return "Child"
    elif age<20:
        return "Teen"
    elif age<30:
        return "Young Adult"
    elif age<50:
        return "Adult"
    return "Senior"

def get_zodiac_sign(day, month):
    zodiac=[
        ("Capricorn",20),("Aquarius",19),("Pisces", 20), 
        ("Aries", 20),("Taurus",21),("Gemini",21),("Cancer",23),
        ("Leo",23),("Virgo",23),("Libra",23),("Scorpio",22),
        ("Sagittarius",22), ("Capricorn",31)
    ]
    if day<zodiac[month-1][1]:
        return zodiac[month-1][0]
    else:
        return zodiac[month][0]

def load_traits(file_path='traits.txt'):
    with open(file_path,'r', encoding='utf-8') as file:
        lines=file.readlines()
    traits={"Generation":{},"Zodiac":{},"AgeGroup":{},"Emotion":{}}
    current_section=None
    for line in lines:
        line=line.strip()
        if not line:
            continue
        if line.startswith('[') and line.endswith(']'):
            current_section=line[1:-1]
        elif ':' in line and current_section:
            key,value=line.split(':',1)
            traits[current_section][key.strip()]=[v.strip() for v in value.split('|')]
    return traits

def get_summary_points(traits, generation, zodiac, age_group, emotion):
    gen=traits["Generation"].get(generation,[""])
    zod=traits["Zodiac"].get(zodiac,[""])
    age=traits["AgeGroup"].get(age_group,[""])
    emot=traits["Emotion"].get(emotion.lower(),[""])
    return[
        random.choice(emot),
        random.choice(age),
        random.choice(zod),
        random.choice(gen)
    ]

def create_personality_card(traits, summary, generation, face_img_path=None, output_path="personalityCard.png"):
    w, h = 600,400
    bg_color="beige"
    title_color=(255,140,0)
    text_color = (25,25,112)
    border_color = (200, 180, 140)  
    box_color = (255,248,220)  
    img = Image.new("RGB", (w, h),bg_color)
    draw = ImageDraw.Draw(img)

    # Fonts
    title_font = ImageFont.truetype("seguiemj.ttf", 30)
    text_font = ImageFont.truetype("seguiemj.ttf", 18)
    sub_font=ImageFont.truetype("seguiemj.ttf",26)

    title_text = "✨ Personality Snapshot ✨"
    title_width = draw.textlength(title_text, font=title_font)
    draw.text(((w - title_width) // 2, 20), title_text, font=title_font, fill=title_color)
    
    # Face Image
    if face_img_path:
        face = Image.open(face_img_path).convert("RGB").resize((100, 100))
        img.paste(face, (w - 120, 60))
        
    # Summary Box
    x=15
    y=180
    box_width = w - 30
    box_height = len(summary) * 35 + 40
    draw.rounded_rectangle(
        [x, y, x + box_width, y + box_height],
        radius=17,
        fill=box_color,
        outline=border_color,
        width=2
    )

    draw.text((x + 10, y+10), "Impression", font=sub_font, fill=title_color)
    y += 50
    for point in summary:
        lines = textwrap.wrap(point, width=60)
        for i, line in enumerate(lines):
            bullet = "• " if i == 0 else "  "
            draw.text((x + 20, y), f"{bullet}{line}", font=text_font, fill=text_color)
            y += 26
   
    #img.save(output_path)
    #print(f"Personality card saved as:{output_path}")