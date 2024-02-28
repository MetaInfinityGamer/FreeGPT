# -*- coding: utf-8 -*-
import logging
import os
import re
from time import sleep

from langchain.callbacks import StreamlitCallbackHandler
from langchain.chains import LLMChain
from streamlit_card import card
import openai
import streamlit as st
from streamlit_chat import message
import streamlit.components.v1 as components
import streamlit_antd_components as sac
import pandas as pd
from PIL import Image
import streamlit as st
from streamlit_drawable_canvas import st_canvas

#右上角可以调整黑夜模式和白天模式，默认为黑夜模式
st.set_page_config(
    page_title="Cool App  Power By Everyone",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.FreeGPT.com/help',
        'Report a bug': "https://www.FreeGPT.com/bug",
        'About': "# Free GPT And SD"
    }
)