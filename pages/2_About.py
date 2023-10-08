import streamlit as st

st.set_page_config(page_title="About GalaxyGrooves", page_icon="🎶")

header = ("# Enjoyed listening to Galaxy Groove?  \n"
          "Here's the methodology behind how we created those *galactic* sounds!")
st.markdown(header)



st.header("WISE: Our Data Source", divider='orange')
st.markdown("We used data recorded by NASA's Wide-field Infrared Survey Explorer (WISE).  \n"
            "The WISE telescope measures 4 different types of wavelength bands: 3.4, 4.6, 12, and 22μm wavelength range bands.  \n"
            "Each band wavelength corresponds to a range of thermal activity.  \n"
            "For example,  \n"
            "- Band 1 (3.4μm): Broad-band sensitivity to stars and galaxies  \n"
            "- Band 2 (4.6μm): Sub-stellar objects such as brown dwarfs  \n"
            "- Band 3 (12μm): Detects thermal radiation from asteroids  \n"
            "- Band 4 (22μm): Sensitivity to dust in star-forming regions  \n"
            "[Source](https://en.wikipedia.org/wiki/Wide-field_Infrared_Survey_Explorer)")

st.header("Our Sonification Process", divider='orange')
st.markdown("")





# band 1 pitch, new pitch, new note
# band 2 length of the note, higher intensity equals longer note
# band 3 open to any features
# band 4 higher the concentration of dust, louder volume
