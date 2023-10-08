import streamlit as st

st.set_page_config(page_title="About GalaxyGrooves", page_icon="🎶")

header = ""

st.markdown("# Enjoyed listening to that Galaxy Groove?  "
            "Here's the methodology behind how we create those galactic sounds!")

st.markdown("## Our Data Source"
            "We used data from the Wide-field Infrared Survey Explorer (WISE) from NASA."
            "The telescope measures 4 different types of wavelength bands: 3.4, 4.6, 12, and 22μm wavelength range bands."
            "Each band wavelength "
            "")


# band 1 pitch, new pitch, new note
# band 2 length of the note, higher intensity equals longer note
# band 3 open to any features
# band 4 higher the concentration of dust, louder volume
