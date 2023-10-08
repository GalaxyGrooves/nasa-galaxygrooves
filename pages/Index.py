import streamlit as st
from PIL import Image
import subprocess


st.write("""
    # galaxy_grooves Test
""")


def getM45():
    band1 = Image.open('/static/M45/band1.png')
    if band1.mode != "RGB":
        band1 = band1.convert("RGB")
    band2 = Image.open('/nasa-galaxygrooves/static/M45/band2.png')
    if band2.mode != "RGB":
        band2 = band2.convert("RGB")
    band4 = Image.open('/nasa-galaxygrooves/static/M45/band4.png')
    if band4.mode != "RGB":
        band4 = band4.convert("RGB")
    col4, col5, col6 = st.columns(3)
    with col4:
        st.image(band1, caption='band 1', width=150)
    with col5:
        st.image(band2, caption='band 2', width=150)
    with col6:
        st.image(band4, caption='band 4', width=150)
    command = ["python", "rgb.py", "/nasa-galaxygrooves/static/M45/band1.png", '/nasa-galaxygrooves/static/M45/band2.png', '/nasa-galaxygrooves/static/M45/band4.png']
    subprocess.run(command)

def getM33():
    band1 = Image.open('/nasa-galaxygrooves/static/M33/band1.png')
    if band1.mode != "RGB":
        band1 = band1.convert("RGB")
    band2 = Image.open('/nasa-galaxygrooves/static/M33/band2.png')
    if band2.mode != "RGB":
        band2 = band2.convert("RGB")
    band4 = Image.open('/nasa-galaxygrooves/static/M33/band4.png')
    if band4.mode != "RGB":
        band4 = band4.convert("RGB")
    col4, col5, col6 = st.columns(3)
    with col4:
        st.image(band1, caption='band 1', width=150)
    with col5:
        st.image(band2, caption='band 2', width=150)
    with col6:
        st.image(band4, caption='band 4', width=150)
    subprocess.run(["python", "rgb.py", '/nasa-galaxygrooves/static/M33/band1.png', '/nasa-galaxygrooves/static/M33/band2.png', '/nasa-galaxygrooves/static/M33/band4.png'])


def getNCG_1365():
    band1 = Image.open('/nasa-galaxygrooves/static/NGC 1365/NGC 1365 Band 1.png')
    if band1.mode != "RGB":
        band1 = band1.convert("RGB")
    band2 = Image.open('/nasa-galaxygrooves/static/NGC 1365/NGC 1365 Band 2.png')
    if band2.mode != "RGB":
        band2 = band2.convert("RGB")
    band4 = Image.open('/nasa-galaxygrooves/static/NGC 1365/NGC 1365 Band 4.png')
    if band4.mode != "RGB":
        band4 = band4.convert("RGB")
    col4, col5, col6 = st.columns(3)
    with col4:
        st.image(band1, caption='band 1', width=150)
    with col5:
        st.image(band2, caption='band 2', width=150)
    with col6:
        st.image(band4, caption='band 4', width=150)
    subprocess.run(["python", "rgb.py", '/nasa-galaxygrooves/static/NGC 1365/NGC 1365 Band 1.png', '/nasa-galaxygrooves/static/NGC 1365/NGC 1365 Band 2.png', '/nasa-galaxygrooves/static/NGC 1365/NGC 1365 Band 4.png'])

def getNCG_1097():
    band1 = Image.open('/nasa-galaxygrooves/static/NCG 1097 /band1.png')
    if band1.mode != "RGB":
        band1 = band1.convert("RGB")
    band2 = Image.open('/nasa-galaxygrooves/static/NCG 1097 /band2.png')
    if band2.mode != "RGB":
        band2 = band2.convert("RGB")
    band4 = Image.open('/nasa-galaxygrooves/static/NCG 1097 /band4.png')
    if band4.mode != "RGB":
        band4 = band4.convert("RGB")
    col4, col5, col6 = st.columns(3)
    with col4:
        st.image(band1, caption='band 1', width=150)
    with col5:
        st.image(band2, caption='band 2', width=150)
    with col6:
        st.image(band4, caption='band 4', width=150)
    subprocess.run(["python", "rgb.py", '/nasa-galaxygrooves/static/NCG 1097 /band1.png', '/nasa-galaxygrooves/static/NCG 1097 /band2.png', '/nasa-galaxygrooves/static/NCG 1097 /band4.png'])


col1, col2 = st.columns(2)
M33 = Image.open('/nasa-galaxygrooves/static/M33/color.png')
M45 = Image.open('/nasa-galaxygrooves/static/M45/color.png')
NCG_1097 = Image.open('/nasa-galaxygrooves/static/NCG 1097 /color.png')
NGC_1365 = Image.open('/nasa-galaxygrooves/static/NGC 1365/NGC 1365 color.png')

with col1:
    m33_bool = False
    ngc_1365 = False
    st.image(M33, caption='M33', width = 300,)
    if st.button("Select Star", key='M33'):
        m33_bool = True
    st.image(NGC_1365, caption='NGC 1365', width = 300,)
    if st.button("Select Star", key='NGC 1365'):
        ngc_1365 = True
if m33_bool == True:
    getM33()
if ngc_1365 == True:
    getNCG_1365()



with col2:
    m45 = False
    ncg_1097 = False
    st.image(M45, caption='M45', width = 300,)
    st.text("")
    st.text("")
    st.text("")
    if st.button("Select Star", key='M45'):
        m45 = True
    st.text("")
    st.text("")
    st.text("")
    st.image(NCG_1097, caption='NCG 1097', width = 300)
    if st.button("Select Star", key='NCG 1097'):
        ncg_1097 = True
if m45 == True:
    getM45()
if ncg_1097 == True:
    getNCG_1097()


