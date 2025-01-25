import python_avatars as pa
import streamlit as st
import base64
from random import randrange

st.set_page_config(page_title="Avatar Maker", layout="wide")

st.header("Avatar Maker")

st.sidebar.header("Customize your avatar")

style = st.sidebar.selectbox("style", ("CIRCLE", "TRANSPARENT"), index=1)

skin_color = ["TANNED", "YELLOW", "LIGHT", "PALE", "BLACK"]

hair_type = [
    "SHORT_WAVED",
    "SHORT_FLAT",
    "SHORT_DREADS_1",
    "SHORT_DREADS_2",
    "SHORT_CURLY",
    "BOB",
    "STRAIGHT_2",
    "BIG_HAIR",
    "BRAIDS",
    "BUN",
    "BUZZCUT",
    "CURLY",
    "CURLY_2",
    "FRO_BAND",
    "HAT",
    "TWIST_LONG_HAIR_2",
    "LONG_HAIR_CURLY",
    "MOHAWK",
    "NONE",
    "FRIZZLE",
    "MOWGLI",
    "FRO",
]

hair_color = [
    "BLACK",
    "RED",
    "AUBURN",
    "SILVER_GRAY",
    "PASTEL_PINK",
    "BLONDE_GOLDEN",
    "BLONDE_GOLDEN",
    "BLONDE",
    "BROWN",
]

hat_type = [
    "WINTER_HAT_1",
    "WINTER_HAT_2",
    "WINTER_HAT_3",
    "WINTER_HAT_4",
    "TURBAN",
    "HIJAB",
    "CHEF_CAP",
    "HAT",
]

hat_color = [
    "BLACK",
    "PASTEL_PINK",
    "BLUE_01",
    "BLUE_02",
    "BLUE_03",
    "PASTEL_RED",
    "PASTEL_YELLOW",
    "BLONDE",
]

mouth_type = [
    "DEFAULT",
    "CONCERNED",
    "DISBELIEF",
    "EATING",
    "SAD",
    "GRIMACE",
    "SCREAM_OPEN",
    "SMILE",
    "TONGUE",
]

eye_type = [
    "DEFAULT",
    "CLOSED",
    "CRY",
    "X_DIZZY",
    "HAPPY",
    "HEART",
    "EYE_ROLL",
    "SIDE",
    "SQUINT",
    "WINK",
    "WINK_WACKY",
]

cloth_type = [
    "SHIRT_WICK",
    "JEDI_ROBE",
    "GLADIATOR",
    "BOND_SUIT",
    "ASTRONAUT_SUIT",
    "BLAZER_SWEATER",
    "BLAZER_SHIRT",
    "HOODIE",
    "COLLAR_SWEATER",
    "OVERALL",
    "SHIRT_CREW_NECK",
    "CHEF",
]

cloth_color = [
    "BLACK",
    "PINK",
    "RED",
    "WHITE",
    "GRAY_01",
    "GRAY_02",
    "HEATHER",
    "PASTEL_BLUE",
    "BLUE_01",
    "BLUE_02",
    "BLUE_03",
    "PASTEL_GREEN",
    "PASTEL_YELLOW",
    "PASTEL_ORANGE",
]

if st.button("Create Random"):
    selected_skin_color = st.sidebar.selectbox("type", skin_color, index=2)
    selected_hair_type = st.sidebar.selectbox(
        "hair type", hair_type, index=randrange(0, len(hair_type))
    )
    selected_hair_color = st.sidebar.selectbox(
        "hair color", hair_color, index=randrange(0, len(hair_color))
    )
    selected_mouth_type = st.sidebar.selectbox(
        "mouth", mouth_type, index=randrange(0, len(mouth_type))
    )
    selected_eye_type = st.sidebar.selectbox(
        "eye", eye_type, index=randrange(0, len(eye_type))
    )
    selected_cloth_type = st.sidebar.selectbox(
        "cloth", cloth_type, index=randrange(0, len(cloth_type))
    )
    selected_cloth_color = st.sidebar.selectbox(
        "cloth color", cloth_color, index=randrange(0, len(cloth_color))
    )
else:
    selected_skin_color = st.sidebar.selectbox("skin color", skin_color, index=2)
    # list_color = st.sidebar.selectbox('color',list_color,index= 0)
    selected_hair_type = st.sidebar.selectbox("hair type", hair_type, index=0)
    selected_hair_color = st.sidebar.selectbox("hair color", hair_color, index=0)
    # hat_color = st.sidebar.selectbox('hat',hat_color,index= 0)
    selected_mouth_type = st.sidebar.selectbox("mouth", mouth_type, index=0)
    selected_eye_type = st.sidebar.selectbox("eye", eye_type, index=0)
    selected_cloth_type = st.sidebar.selectbox("cloth", cloth_type, index=0)
    selected_cloth_color = st.sidebar.selectbox("cloth color", cloth_color, index=0)

avatar = pa.Avatar(
    style=eval("pa.AvatarStyle.%s" % style),
    skin_color=eval("pa.SkinColor.%s" % selected_skin_color),
    top=eval("pa.HairType.%s" % selected_hair_type),
    hair_color=eval("pa.HairColor.%s" % selected_hair_color),
    eyes=eval("pa.EyeType.%s" % selected_eye_type),
    mouth=eval("pa.MouthType.%s" % selected_mouth_type),
    clothing=eval("pa.ClothingType.%s" % selected_cloth_type),
    clothing_color=eval("pa.ClothingColor.%s" % selected_cloth_color),
)


rendered_avatar = avatar.render("avatar.svg")

with open("avatar.svg", "r") as svg_file:
    svg_data = svg_file.read()


st.components.v1.html(f"<div>{svg_data}</div>", height=400)


def imagedownload(svg_data):
    b64 = base64.b64encode(svg_data.encode()).decode()
    href = f'<a href="data:image/svg+xml;base64,{b64}" download="avatar.svg">Download avatar</a>'
    return href


st.markdown(imagedownload(svg_data), unsafe_allow_html=True)


st.info(
    """
**Note:** 

After downloading the file, please use free online tools such as 
[Convertio](https://convertio.co/) or [Online Convert](https://image.online-convert.com/convert-to-png) to convert it to an image.
***
* Programmer: Moein Zanjirian Zadeh

* Email: moeinz9322@gmail.com   
"""
)
