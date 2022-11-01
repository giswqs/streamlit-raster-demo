import streamlit_raster
import streamlit as st
import leafmap

st.set_page_config(layout="wide")

st.title("Streamlit Raster Demo")

m = leafmap.Map()
m.add_local_tile('data/bahamas_rgb.tif')
m.to_streamlit( height=600)