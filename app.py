import streamlit as st
from crew import run_news

st.title("News Reporter AI Agent")

topic = st.text_input(
    "Enter topic",
    value="AI in healthcare"
)

if st.button("Generate News"):

    with st.spinner("Generating..."):

        result = run_news(topic)

        st.write(result)
