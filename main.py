import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd



st.set_page_config(
    page_title="Data Exploration App",
    page_icon="📓",
)

#with st.sidebar:
selected = option_menu(
    menu_title=None,
    options=["Introduction", "Visualizations", "Conclusion"],
    icons=["house", "graph-up", "journal-text"],
    default_index=0,
    orientation="horizontal",
)

if selected == "Introduction":
    st.title("Sleep Health and Lifestyle")
    st.markdown("""<div style="text-align: justify;">
        Sleep is a fundamental component of human health, affecting physical well-being, cognitive performance, and emotional stability. In recent years, the study of sleep health has gained significant attention as researchers and healthcare professionals aim to understand how sleep patterns influence overall lifestyle and well-being. The Sleep Health and Lifestyle Dataset is designed to explore the intricate relationship between individuals' sleep habits and their broader lifestyle choices, providing valuable insights for improving sleep quality and promoting healthier living. The dataset is structured to enable the analysis of correlations between sleep habits and lifestyle behaviors, allowing researchers to explore patterns, identify risk factors for poor sleep, and assess the impact of lifestyle interventions on sleep health. 
        <br><br>This dataset can be utilized by sleep scientists, healthcare professionals, public health policymakers, and data analysts to develop recommendations, tools, and interventions aimed at enhancing both sleep and overall well-being.
    </div>""", unsafe_allow_html=True)

if selected == "Visualizations":
    sleep = pd.read_csv('Sleep_health_and_lifestyle_dataset.csv')
    with st.container():     
        st.subheader("Data Preview")
        st.dataframe(sleep, use_container_width=True)

    
    with st.container():
        col1, col2 = st.columns(2, vertical_alignment="center")
        with col1:
            st.subheader("Sleep Duration by Occupation")
            st.bar_chart(sleep, x="Occupation", y="Sleep Duration", stack=False, use_container_width=True)
        with col2:
            st.subheader("Stress Level by Occupation")
            st.bar_chart(sleep, x="Occupation", y="Stress Level", stack=False, use_container_width=True)
    
    with st.container():
        st.bar_chart(sleep, y="Age", x="BMI Category", color="Gender", stack=False, use_container_width=True)

if selected == "Conclusion":
    st.subheader("Conclusion")
    st.markdown("""
        <div style="text-align: justify;">The Sleep Health and Lifestyle Dataset offers a comprehensive resource for examining the complex interplay between sleep habits and lifestyle choices. By integrating diverse factors such as sleep duration, quality, health metrics, and daily behaviors, this dataset enables a deeper understanding of how lifestyle affects sleep health and how sleep impacts overall well-being.
        <br><br>Insights gleaned from this dataset can inform targeted interventions aimed at improving sleep hygiene and lifestyle choices. Researchers and health professionals can utilize the data to develop personalized sleep recommendations, identify risk factors for sleep disorders, and design holistic strategies to enhance both physical and mental health.
        <br><br>Ultimately, this dataset provides a valuable foundation for improving public awareness about the importance of sleep and fostering healthier lifestyles, contributing to better long-term health outcomes and quality of life.
    </div>""", unsafe_allow_html=True)
