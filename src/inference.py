import streamlit as st
import pandas as pd
from pipeline import WebtoonRecommender
import time

@st.cache_resource
def load_recommender():
    rec = WebtoonRecommender()
    rec.load_data()
    rec.preprocess_and_engineer()
    rec.build_model()
    return rec

st.title("Webtoon Recommendation System")

recommender = load_recommender()

title_input = st.text_input("Enter a webtoon title (Example: Chainsaw Man):")

if st.button("Get Recommendations"):
    if title_input.strip() == "":
        st.warning("Please enter a title.")
    else:
        with st.spinner("Getting the reccomendations..."):
            results = recommender.get_recommendations(title_input)
            time.sleep(0.2)

        if isinstance(results, str):
            st.error(results)
        else:
            st.success("Reccomendations are ready!")
            st.dataframe(results)
