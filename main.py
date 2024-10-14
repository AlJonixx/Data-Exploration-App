import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px



st.set_page_config(
    page_title="Sleep Health and Lifestyle",
    page_icon="📓",
    layout="centered",
)

# Menu bar
selected = option_menu(
    menu_title=None,
    options=["Introduction", "Visualizations", "Conclusion"],
    icons=["house", "graph-up", "journal-text"],
    default_index=0,
    orientation="horizontal",
)

# Introduction Section
if selected == "Introduction":
    st.title("Sleep Health and Lifestyle")
    st.markdown("""<div style="text-align: justify;">
        Sleep is a fundamental component of human health, affecting physical well-being, cognitive performance, and emotional stability. In recent years, the study of sleep health has gained significant attention as researchers and healthcare professionals aim to understand how sleep patterns influence overall lifestyle and well-being. The Sleep Health and Lifestyle Dataset is designed to explore the intricate relationship between individuals' sleep habits and their broader lifestyle choices, providing valuable insights for improving sleep quality and promoting healthier living. The dataset is from Kaggle and is structured to enable the analysis of correlations between sleep habits and lifestyle behaviors, allowing researchers to explore patterns, identify risk factors for poor sleep, and assess the impact of lifestyle interventions on sleep health. 
        <br><br>This dataset can be utilized by sleep scientists, healthcare professionals, public health policymakers, and data analysts to develop recommendations, tools, and interventions aimed at enhancing both sleep and overall well-being.
    </div>""", unsafe_allow_html=True)

# Visualizaiton Section
if selected == "Visualizations":
    sleep = pd.read_csv('Sleep_health_and_lifestyle_dataset.csv')
    with st.container():     
        st.subheader("Data Preview")
        st.dataframe(sleep, use_container_width=True)

    st.divider()
    with st.container():
        selected_col = st.selectbox("Select variable to display on bar chart", ['Sleep Duration', 'Stress Level'])

        st.subheader(f"**{selected_col}** by Occupation")
        st.bar_chart(sleep, x="Occupation", 
                    y=selected_col, 
                    stack=False, 
                    use_container_width=True)
        
        st.markdown("""<div style="text-align:justify;">
            <h3>Insights</h3>
            <h5>Sleep Duration by Occupation</h5>
            <ul><li><b>Doctors, Engineers, and Nurses</b> appear to have the highest average sleep duration, around 7-8 hours per night, indicating better sleep health.</li>
            <li><b>Managers, Sales Representatives, and Software Engineers</b> tend to have shorter sleep durations, around 6 hours or slightly less. This suggests that individuals in these roles may face more challenges in achieving adequate sleep.</li>
            <li><b>Salespersons</b> seem to have the lowest sleep duration, potentially reflecting high work demands or stress in this profession, which may negatively impact sleep.</li>
            </ul><br>
            <h5>Stress Level by Occupation</h5>
            <ul><li><b>Salespersons, Scientists, and Software Engineers</b> report the highest levels of stress, with stress levels reaching close to 8 on the scale. These occupations may involve high workloads, deadlines, or complex problem-solving, contributing to their elevated stress levels.</li>
            <li><b>Doctors, Engineers, and Nurses</b> also have high stress levels, although they still manage to get relatively good sleep despite their stressful jobs.</li>
            <li><b>Managers and Lawyers</b> show moderate stress levels, while Teachers and Accountants seem to experience slightly lower levels of stress in comparison to others.</li>
            </ul><br>
        </div>""", unsafe_allow_html=True)
    
    st.divider()
    with st.container():
        st.subheader("Physical Activity Level by BMI Category")
        st.bar_chart(sleep, 
                    y="Physical Activity Level", 
                    x="BMI Category", 
                    color="Gender", 
                    stack=False, 
                    use_container_width=True)
        
        st.markdown("""<div style="text-align:justify;">
            The chart shows Physical Activity Levels across different BMI categories (Normal, Normal Weight, Obese, and Overweight) separated by gender (light blue for females, dark blue for males).
            <h3>Key Insights</h3>
            <ul>
                <li>Physical activity tends to decrease as BMI increases, especially for individuals in the obese category.</li>
                <li>Males generally exhibit higher physical activity levels than females in most BMI categories, except for the normal weight and overweight category where females are more active.</li>
                <li>The normal weight group is the most physically active, suggesting a strong association between maintaining a healthy weight and engaging in regular physical activity.</li>
                <li>The reduced activity in the obese and overweight categories highlights a potential area for intervention, as increasing physical activity may help in weight management and overall health.</li>
            </ul>
        </div>""", unsafe_allow_html=True)
    
    with st.container():
        st.divider()
        st.subheader('Sleep Disorder Pie Chart')
        sleep["Sleep Disorder"] = sleep["Sleep Disorder"].fillna('None').replace({0: 'None', 1: 'Insomnia', 2: 'Sleep Apnea'})
        sleepdis = sleep['Sleep Disorder'].value_counts().reset_index()
        sleepdis.columns = ['Sleep Disorder', 'Total']
        fig = px.pie(sleepdis, values='Total', names='Sleep Disorder', title='Sleep Disorder Distribution', color_discrete_sequence=px.colors.qualitative.Set2)
        st.plotly_chart(fig)
        st.divider()

        #Create a Plotly scatter plot
        figplot = px.scatter(sleep, x='Age', 
                            y='Sleep Duration', 
                            color='Sleep Disorder',
                            color_continuous_scale=px.colors.sequential.Sunset,
                            title="Sleep Duration of people with and without Sleep Disorder")
        
        #Center title
        figplot.update_layout(
        title=dict(
            text=f"Sleep Duration of people with and without Sleep Disorder",
            x=0.5,          # Center the title
            xanchor='center',  # Anchor the title at the center
            font=dict(size=20)  # Optional: Set font size for better visibility
            )
        )

        st.plotly_chart(figplot, use_container_width=True)

        st.markdown("""<div style="text-align:justify;">
            These charts shows the distribution of individuals with or without sleep disorders, broken down into three categories: None, Sleep Apnea, and Insomnia.<br><br> <h5>No Sleep Disorder (58.6%)</h5>
                <ul><li>The majority of the population, 58.6%, do not suffer from any sleep disorder. This indicates that most individuals in the dataset experience normal or healthy sleep patterns without any significant disturbances like insomnia or sleep apnea.</li></ul>
            <h5>Sleep Apnea (20.9%)</h5>
                <ul><li>A notable portion (20.9%) of the population experiences sleep apnea, a condition characterized by interruptions in breathing during sleep. This suggests that sleep apnea is a relatively common sleep disorder and could be a significant factor impacting overall sleep quality for many individuals.</li></ul>
            <h5>Insomnia (20.6%)</h5>
                <ul><li>20.6% of the population suffers from insomnia, another common sleep disorder characterized by difficulty in falling asleep or staying asleep. This percentage is very close to the sleep apnea, indicating that insomnia is also a prominent issue affecting people's sleep health.</li></ul>
            <h3>Key Insights</h3>
                <ul>
                    <li>While the majority of individuals (over half) report no sleep disorders, 41.4% of the population struggles with either sleep apnea or insomnia, which are both significant contributors to poor sleep quality.</li>
                    <li>The similar prevalence rates of sleep apnea and insomnia indicate that both disorders are common and need attention in terms of diagnosis, treatment, and management.</li>
                    <li>Given the high proportion of people affected by these sleep disorders, this insight highlights the need for targeted interventions aimed at improving sleep health, such as lifestyle changes, medical treatments, or sleep hygiene education.</li>
                </ul>
                Overall, these insights underscore the importance of addressing sleep health, as a considerable portion of the population is affected by sleep disorders, which can have a profound impact on well-being and daily functioning.
        </div>""", unsafe_allow_html=True)

#Conclusion Section
if selected == "Conclusion":
    st.subheader("Conclusion")
    st.markdown("""
        <div style="text-align: justify;">The Sleep Health and Lifestyle Dataset offers a comprehensive resource for examining the complex interplay between sleep habits and lifestyle choices. By integrating diverse factors such as sleep duration, quality, health metrics, and daily behaviors, this dataset enables a deeper understanding of how lifestyle affects sleep health and how sleep impacts overall well-being.
        <br><br>Insights gathered from this dataset can inform targeted interventions aimed at improving sleep hygiene and lifestyle choices. Researchers and health professionals can utilize the data to develop personalized sleep recommendations, identify risk factors for sleep disorders, and design holistic strategies to enhance both physical and mental health.
        <br><br>Ultimately, this dataset provides a valuable foundation for improving public awareness about the importance of sleep and fostering healthier lifestyles, contributing to better long-term health outcomes and quality of life.
    </div>""", unsafe_allow_html=True)
