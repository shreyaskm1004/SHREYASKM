import streamlit as st
import seaborn as sns
import plotly.express as px
import pandas as pd

# --- Title and Introduction ---
st.title("Interactive Visualizations with Plotly and Streamlit")
st.markdown("""
    <style>
        .main {
            background-color: #2a3d66;
            color: white;
        }
        .sidebar .sidebar-content {
            background-color: #1e2a3d;
        }
        h1, h2, h3, h4, h5 {
            color: #70b7f7;
        }
        .stButton>button {
            background-color: #70b7f7;
            color: white;
        }
        .stTextInput>div>input {
            background-color: #d1e0e0;
        }
    </style>
    """, unsafe_allow_html=True)

# --- Input for Author Information ---
st.sidebar.header("Visualization Skill Workshop - Plotly")
name = st.sidebar.text_input("Enter your name")
usn = st.sidebar.text_input("Enter your roll no.")
instructor_name = st.sidebar.text_input("Course Instructor Name")

# Display author information if provided
if name and usn and instructor_name:
    st.markdown(
        f"<h5>Created by:</h5>"
        f"<p>{name} (USN: {usn})</p>"
        f"<p>Instructor: {instructor_name}</p>",
        unsafe_allow_html=True
    )

# --- Load Dataset ---
tips = sns.load_dataset('tips')  # Loading the tips dataset

# Display the first few rows of the dataset
st.write("## Dataset Overview")
st.write(tips.head())

# --- Task 2: Interactive Bar Chart ---
st.subheader("Task 2: Bar Chart - Average Tip by Day")
# Bar Chart: Average Tip by Day with color for each day
fig2 = px.bar(
    tips, x='day', y='tip', color='day',
    title='Average Tip by Day',
    labels={'tip': 'Average Tip ($)', 'day': 'Day of the Week'},
    template='plotly_white'
)
fig2.update_layout(
    xaxis_title="Day of the Week",
    yaxis_title="Average Tip ($)",
    font=dict(size=14)
)
st.plotly_chart(fig2)  # Display the chart in Streamlit

# --- Task 3: Interactive Histogram ---
st.subheader("Task 3: Histogram - Tip Distribution by Day")
# Histogram: Tip distribution by day with color for each day
fig4 = px.histogram(
    tips, x='tip', color='day',
    title='Tip Distribution by Day',
    labels={'tip': 'Tip Amount ($)', 'day': 'Day of the Week'},
    template='plotly_white'
)
fig4.update_layout(
    xaxis_title="Tip Amount ($)",
    yaxis_title="Frequency",
    font=dict(size=14)
)
st.plotly_chart(fig4)  # Display the chart in Streamlit
