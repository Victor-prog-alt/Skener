import streamlit as st
import easyocr
import numpy as np
from PIL import Image
import cv2
import re
from rapidfuzz import fuzz

========================================
PAGE CONFIG
========================================

st.set_page_config(
    page_title="AI Ingredient Scanner",
    page_icon="🧪",
    layout="centered"
)

========================================
LOAD OCR
========================================

@st.cache_resource
def load_reader():
    return easyocr.Reader(['bg', 'en'])

reader = load_reader()

========================================
DATABASE
========================================

INGREDIENT_DATABASE = {

    # SWEETENERS

    "E950": {
        "en": "Acesulfame K",
        "bg": "Ацесулфам К",
        "risk": 3,
        "category": "Sweetener",
        "info": "Artificial sweetener",
        "aliases": [
            "e950",
            "acesulfame k",
            "ацесулфам",
            "ацесулфам к"
        ]
    },

    "E951
